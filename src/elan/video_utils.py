import cv2
import os
import numpy as np
import datetime
from typing import Union, List, Tuple, Dict, Any, Optional

class video_utils:
    def __init__(self):
        """Video işleme yardımcıları sınıfı"""
        pass

    def _check_video_path(self, video_path: str) -> None:
        """Video dosyasının varlığını kontrol et"""
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video dosyası bulunamadı: {video_path}")
    
    def get_video_info(self, video_path: str) -> Dict[str, Any]:
        """Video hakkında temel bilgileri al
        
        Args:
            video_path: Video dosya yolu
            
        Returns:
            Dictionary: Video bilgilerini içeren sözlük
            {
                'width': genişlik,
                'height': yükseklik,
                'fps': fps,
                'frame_count': toplam kare sayısı,
                'duration': saniye cinsinden süre,
                'codec': codec bilgisi
            }
        """
        self._check_video_path(video_path)
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"{video_path} dosyası açılamadı")
        
        try:
            # Temel özellikleri al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps if fps > 0 else 0
            
            # Codec bilgisi
            fourcc_int = int(cap.get(cv2.CAP_PROP_FOURCC))
            fourcc = chr(fourcc_int & 0xFF) + chr((fourcc_int >> 8) & 0xFF) + \
                     chr((fourcc_int >> 16) & 0xFF) + chr((fourcc_int >> 24) & 0xFF)
            
            return {
                'width': width,
                'height': height,
                'fps': fps,
                'frame_count': frame_count,
                'duration': duration,
                'duration_formatted': str(datetime.timedelta(seconds=int(duration))),
                'codec': fourcc
            }
        finally:
            cap.release()
    
    def extract_frames(self, video_path: str, output_dir: str = None, 
                      frame_interval: int = 1, max_frames: int = None,
                      start_time: float = 0, end_time: float = None,
                      resize: Tuple[int, int] = None) -> List[str]:
        """Videodan belirli aralıklarla kare (frame) çıkarır
        
        Args:
            video_path: Video dosya yolu
            output_dir: Karelerin kaydedileceği dizin (None ise kaydedilmez)
            frame_interval: Kaç karede bir çıkarılacağı (1=tüm kareler)
            max_frames: Çıkarılacak maksimum kare sayısı (None=sınırsız)
            start_time: Başlangıç zamanı (saniye)
            end_time: Bitiş zamanı (saniye) (None=videonun sonuna kadar)
            resize: Kareleri yeniden boyutlandırma (width, height) veya None
            
        Returns:
            List[str]: Eğer output_dir belirtildiyse kaydedilen dosya yolları listesi,
                      aksi halde boş liste
        """
        self._check_video_path(video_path)
        
        # Çıktı klasörü kontrolü
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        saved_frames = []
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            raise ValueError(f"{video_path} dosyası açılamadı")
        
        try:
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Zaman bilgilerini kare indekslerine dönüştür
            start_frame = int(start_time * fps) if start_time > 0 else 0
            end_frame = int(end_time * fps) if end_time is not None else total_frames
            
            # İstenen kareye atla
            if start_frame > 0:
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            
            frame_count = 0
            saved_count = 0
            
            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret or (max_frames is not None and saved_count >= max_frames) or \
                   (frame_count + start_frame >= end_frame):
                    break
                
                if frame_count % frame_interval == 0:
                    # Boyutlandırma işlemi
                    if resize:
                        frame = cv2.resize(frame, resize)
                    
                    # Kareyi kaydet
                    if output_dir:
                        frame_filename = os.path.join(output_dir, f"frame_{saved_count:06d}.jpg")
                        cv2.imwrite(frame_filename, frame)
                        saved_frames.append(frame_filename)
                    
                    saved_count += 1
                
                frame_count += 1
            
            return saved_frames
        finally:
            cap.release()
    
    def create_video_from_frames(self, frames_dir: str, output_video: str, 
                                fps: float = 30.0, frame_pattern: str = "frame_%06d.jpg",
                                codec: str = "mp4v", resize: Tuple[int, int] = None) -> bool:
        """Görüntü karelerinden video oluştur
        
        Args:
            frames_dir: Görüntü karelerinin bulunduğu dizin
            output_video: Oluşturulacak video dosyasının yolu
            fps: Saniyedeki kare sayısı
            frame_pattern: Kare dosyalarının isim formatı
            codec: Video codec'i (FOURCC kodu - 'mp4v', 'XVID', 'avc1', vb.)
            resize: Kareleri yeniden boyutlandırma (width, height) veya None
            
        Returns:
            bool: Başarılı ise True
        """
        if not os.path.exists(frames_dir):
            raise FileNotFoundError(f"Kare dizini bulunamadı: {frames_dir}")
        
        # İlk kareyi oku (çözünürlük için)
        frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(('.jpg', '.jpeg', '.png'))])
        if not frame_files:
            raise ValueError(f"{frames_dir} dizininde görüntü dosyası bulunamadı")
        
        sample_frame = cv2.imread(os.path.join(frames_dir, frame_files[0]))
        height, width = sample_frame.shape[:2]
        
        # Yeniden boyutlandırma
        if resize:
            width, height = resize
        
        # VideoWriter nesnesi oluştur
        fourcc = cv2.VideoWriter_fourcc(*codec)
        
        # Çıktı dizinini kontrol et ve oluştur
        output_dir = os.path.dirname(output_video)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
        
        try:
            # Tüm kareleri ekle
            for frame_file in frame_files:
                frame = cv2.imread(os.path.join(frames_dir, frame_file))
                
                if resize:
                    frame = cv2.resize(frame, resize)
                
                out.write(frame)
            
            return True
        finally:
            out.release()
    
    def convert_video(self, input_video: str, output_video: str, 
                     codec: str = "mp4v", resize: Tuple[int, int] = None,
                     fps: float = None, bitrate: str = None) -> bool:
        """Bir videoyu farklı bir formata veya özelliklerle dönüştür
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Çıkış video dosyası yolu
            codec: Video codec'i (FOURCC kodu - 'mp4v', 'XVID', 'avc1', vb.)
            resize: Yeni boyut (width, height) veya None
            fps: Yeni fps değeri veya None (değişmez)
            bitrate: Video bit hızı (örn. "1M", "2M") veya None
            
        Returns:
            bool: Başarılı ise True
        """
        self._check_video_path(input_video)
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            original_fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Yeni parametre değerlerini ayarla
            if resize:
                width, height = resize
            
            if fps is None:
                fps = original_fps
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # Bitrate belirleme (OpenCV doğrudan desteklemez)
            if bitrate:
                out.set(cv2.VIDEOWRITER_PROP_QUALITY, 100)  # En yüksek kalite
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                if resize:
                    frame = cv2.resize(frame, resize)
                
                out.write(frame)
            
            return True
        finally:
            cap.release()
            if 'out' in locals():
                out.release()
    
    def trim_video(self, input_video: str, output_video: str, 
                  start_time: float, end_time: float,
                  codec: str = "mp4v") -> bool:
        """Videoyu belirli bir zaman aralığında kırp
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Çıkış video dosyası yolu
            start_time: Başlangıç zamanı (saniye)
            end_time: Bitiş zamanı (saniye)
            codec: Video codec'i
            
        Returns:
            bool: Başarılı ise True
        """
        self._check_video_path(input_video)
        
        if start_time >= end_time:
            raise ValueError("Başlangıç zamanı bitiş zamanından küçük olmalıdır")
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Zaman bilgilerini kare indekslerine dönüştür
            start_frame = int(start_time * fps)
            end_frame = int(end_time * fps)
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # İstenen kareye atla
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            
            current_frame = start_frame
            
            while current_frame < end_frame:
                ret, frame = cap.read()
                if not ret:
                    break
                
                out.write(frame)
                current_frame += 1
            
            return True
        finally:
            cap.release()
            if 'out' in locals():
                out.release()
    
    def apply_filter_to_video(self, input_video: str, output_video: str,
                             filter_type: str, codec: str = "mp4v",
                             **filter_params) -> bool:
        """Videoya filtre uygula
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Çıkış video dosyası yolu
            filter_type: Filtre tipi ('grayscale', 'sepia', 'negative', 'blur', vb.)
            codec: Video codec'i
            **filter_params: Filtreye özel parametreler
            
        Returns:
            bool: Başarılı ise True
        """
        self._check_video_path(input_video)
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            
            # Gri tonlama filtresi için kanal sayısını ayarla
            if filter_type == 'grayscale':
                out = cv2.VideoWriter(output_video, fourcc, fps, (width, height), isColor=False)
            else:
                out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Filtreyi uygula
                if filter_type == 'grayscale':
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                elif filter_type == 'blur':
                    kernel_size = filter_params.get('kernel_size', 5)
                    blur_type = filter_params.get('blur_type', 'gaussian')
                    
                    if kernel_size % 2 == 0:
                        kernel_size += 1
                    
                    if blur_type == 'gaussian':
                        frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
                    elif blur_type == 'median':
                        frame = cv2.medianBlur(frame, kernel_size)
                    elif blur_type == 'box':
                        frame = cv2.blur(frame, (kernel_size, kernel_size))
                
                elif filter_type == 'sepia':
                    # Sepya filtresi
                    sepia_kernel = np.array([
                        [0.272, 0.534, 0.131],
                        [0.349, 0.686, 0.168],
                        [0.393, 0.769, 0.189]
                    ])
                    frame = cv2.transform(frame, sepia_kernel)
                
                elif filter_type == 'negative':
                    # Negatif filtresi
                    frame = cv2.bitwise_not(frame)
                
                elif filter_type == 'edge':
                    # Kenar tespiti
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    threshold1 = filter_params.get('threshold1', 100)
                    threshold2 = filter_params.get('threshold2', 200)
                    edges = cv2.Canny(gray, threshold1, threshold2)
                    
                    # Kenarları renkli görüntüye çevir
                    if filter_params.get('color_edges', True):
                        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
                    else:
                        frame = edges
                
                elif filter_type == 'cartoon':
                    # Karikatür efekti
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    gray = cv2.medianBlur(gray, 5)
                    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                                cv2.THRESH_BINARY, 9, 9)
                    color = cv2.bilateralFilter(frame, 9, 300, 300)
                    frame = cv2.bitwise_and(color, color, mask=edges)
                
                elif filter_type == 'brightness':
                    # Parlaklık ayarı
                    factor = filter_params.get('factor', 1.0)
                    frame = cv2.convertScaleAbs(frame, alpha=factor, beta=0)
                
                elif filter_type == 'contrast':
                    # Kontrast ayarı
                    factor = filter_params.get('factor', 1.0)
                    mean = np.mean(frame)
                    frame = cv2.convertScaleAbs(frame, alpha=factor, beta=(1.0-factor) * mean)
                
                # Gri tonlama için RGB'ye dönüştürme (gerekirse)
                if filter_type == 'grayscale' and out.get(cv2.VIDEOWRITER_PROP_IS_COLOR):
                    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                
                out.write(frame)
            
            return True
        finally:
            cap.release()
            if 'out' in locals():
                out.release()
    
    def detect_motion(self, input_video: str, output_video: str = None,
                     sensitivity: float = 20.0, blur_size: int = 21,
                     min_area: int = 500, start_frame: int = 0) -> List[Dict[str, Any]]:
        """Videoda hareket algılama
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Hareketin işaretlendiği video çıktısı (None=kaydetmez)
            sensitivity: Hareket hassasiyeti (düşük=daha hassas)
            blur_size: Bulanıklaştırma boyutu (gürültü azaltma için)
            min_area: Minimum hareket alanı (piksel kare)
            start_frame: Başlangıç kare indeksi
            
        Returns:
            List[Dict]: Tespit edilen hareket anları
            [
                {
                    'frame': kare numarası,
                    'timestamp': zaman damgası (sn),
                    'contours': kontür sayısı,
                    'max_area': en büyük hareket alanı
                },
                ...
            ]
        """
        self._check_video_path(input_video)
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        motions = []
        out = None
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # İstenen kareye atla
            if start_frame > 0:
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            
            # Çıkış videosu ayarla
            if output_video:
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                
                # Çıktı dizinini kontrol et ve oluştur
                output_dir = os.path.dirname(output_video)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # İlk kareyi oku
            ret, frame = cap.read()
            if not ret:
                return motions
            
            # İlk kareyi referans olarak belirle
            prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            prev_frame = cv2.GaussianBlur(prev_frame, (blur_size, blur_size), 0)
            
            frame_count = start_frame
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Gri tonlama ve bulanıklaştırma
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
                
                # Kareler arasındaki farkı hesapla
                frame_delta = cv2.absdiff(prev_frame, gray)
                thresh = cv2.threshold(frame_delta, sensitivity, 255, cv2.THRESH_BINARY)[1]
                
                # Dilation ile boşlukları doldur
                thresh = cv2.dilate(thresh, None, iterations=2)
                
                # Konturları bul
                contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                has_motion = False
                motion_areas = []
                
                # Minimum alandan büyük konturları işaretle
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area < min_area:
                        continue
                    
                    has_motion = True
                    motion_areas.append(area)
                    
                    if output_video:
                        (x, y, w, h) = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Hareket tespit edildiyse kaydet
                if has_motion:
                    timestamp = frame_count / fps
                    motion_info = {
                        'frame': frame_count,
                        'timestamp': timestamp,
                        'timestamp_formatted': str(datetime.timedelta(seconds=int(timestamp))),
                        'contours': len(motion_areas),
                        'max_area': max(motion_areas) if motion_areas else 0
                    }
                    motions.append(motion_info)
                
                # Çıkış videosu oluştur
                if output_video:
                    # Bilgileri ekrana yaz
                    cv2.putText(frame, f"Hareket: {'Var' if has_motion else 'Yok'}", 
                              (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                              (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
                    
                    out.write(frame)
                
                # Şimdiki kareyi bir sonraki için referans olarak ayarla
                prev_frame = gray
            
            return motions
        finally:
            cap.release()
            if out is not None:
                out.release()
    
    def add_text_to_video(self, input_video: str, output_video: str,
                         text: str, position: Tuple[int, int] = (10, 30),
                         font_scale: float = 1.0, color: Tuple[int, int, int] = (0, 255, 0),
                         thickness: int = 2, codec: str = "mp4v") -> bool:
        """Videoya metin ekle
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Çıkış video dosyası yolu
            text: Eklenecek metin
            position: Metin konumu (x, y)
            font_scale: Yazı tipi boyutu
            color: Metin rengi (BGR formatında)
            thickness: Metin kalınlığı
            codec: Video codec'i
            
        Returns:
            bool: Başarılı ise True
        """
        self._check_video_path(input_video)
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Metni ekle
                cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 
                          font_scale, color, thickness, cv2.LINE_AA)
                
                out.write(frame)
            
            return True
        finally:
            cap.release()
            if 'out' in locals():
                out.release()
    
    def speed_change(self, input_video: str, output_video: str, 
                   speed_factor: float, codec: str = "mp4v") -> bool:
        """Video hızını değiştir
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Çıkış video dosyası yolu
            speed_factor: Hız faktörü (1.0=normal, 0.5=yavaş, 2.0=hızlı)
            codec: Video codec'i
            
        Returns:
            bool: Başarılı ise True
        """
        self._check_video_path(input_video)
        
        if speed_factor <= 0:
            raise ValueError("Hız faktörü 0'dan büyük olmalıdır")
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Yeni FPS değeri
            new_fps = fps
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_video, fourcc, new_fps, (width, height))
            
            # Kare sayacı
            count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Hızlandırma: belirli kareleri atla
                # Yavaşlatma: belirli kareleri tekrarla
                if speed_factor > 1.0:  # Hızlandırma
                    if count % speed_factor < 1:
                        out.write(frame)
                else:  # Yavaşlatma veya normal hız
                    repeats = int(1 / speed_factor)
                    for _ in range(repeats):
                        out.write(frame)
                
                count += 1
            
            return True
        finally:
            cap.release()
            if 'out' in locals():
                out.release()
    
    def combine_videos(self, video_paths: List[str], output_video: str,
                      transition_frames: int = 10, codec: str = "mp4v",
                      resize: Tuple[int, int] = None) -> bool:
        """Birden fazla videoyu birleştir
        
        Args:
            video_paths: Birleştirilecek video dosyalarının yolları
            output_video: Çıkış video dosyası yolu
            transition_frames: Geçiş kare sayısı (0=geçiş yok)
            codec: Video codec'i
            resize: Tüm videoları belirli bir boyuta getir (width, height) veya None
            
        Returns:
            bool: Başarılı ise True
        """
        if not video_paths:
            raise ValueError("En az bir video yolu gerekli")
        
        for video_path in video_paths:
            self._check_video_path(video_path)
        
        # Video özelliklerini belirle
        first_cap = cv2.VideoCapture(video_paths[0])
        if not first_cap.isOpened():
            raise ValueError(f"{video_paths[0]} dosyası açılamadı")
        
        try:
            # Ortak özellikler için ilk videoyu referans al
            if resize:
                width, height = resize
            else:
                width = int(first_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(first_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            fps = first_cap.get(cv2.CAP_PROP_FPS)
            
            # Çıktı dizinini kontrol et ve oluştur
            output_dir = os.path.dirname(output_video)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # VideoWriter nesnesi oluştur
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # Tüm videoları birleştir
            for i, video_path in enumerate(video_paths):
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print(f"Uyarı: {video_path} dosyası açılamadı, atlanıyor")
                    continue
                
                # Geçiş için son kareleri sakla
                if transition_frames > 0 and i < len(video_paths) - 1:
                    transition_buffer = []
                
                frame_count = 0
                
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Boyutlandırma
                    if resize or frame.shape[1] != width or frame.shape[0] != height:
                        frame = cv2.resize(frame, (width, height))
                    
                    # Geçiş için son kareleri sakla
                    if transition_frames > 0 and i < len(video_paths) - 1:
                        if frame_count >= cap.get(cv2.CAP_PROP_FRAME_COUNT) - transition_frames:
                            transition_buffer.append(frame.copy())
                    
                    out.write(frame)
                    frame_count += 1
                
                cap.release()
                
                # Geçiş efekti uygula
                if transition_frames > 0 and i < len(video_paths) - 1 and transition_buffer:
                    next_cap = cv2.VideoCapture(video_paths[i+1])
                    if not next_cap.isOpened():
                        continue
                    
                    # Sonraki videodan geçiş kareleri al
                    next_frames = []
                    for _ in range(transition_frames):
                        ret, next_frame = next_cap.read()
                        if not ret:
                            break
                        
                        if resize or next_frame.shape[1] != width or next_frame.shape[0] != height:
                            next_frame = cv2.resize(next_frame, (width, height))
                        
                        next_frames.append(next_frame)
                    
                    next_cap.release()
                    
                    # Geçişi uygula
                    min_frames = min(len(transition_buffer), len(next_frames))
                    for j in range(min_frames):
                        # Alpha değerini hesapla (0->1)
                        alpha = j / min_frames
                        
                        # İki kareyi karıştır
                        blended = cv2.addWeighted(transition_buffer[j], 1 - alpha, 
                                                next_frames[j], alpha, 0)
                        out.write(blended)
            
            return True
        finally:
            first_cap.release()
            if 'out' in locals():
                out.release()
    
    def detect_faces_in_video(self, input_video: str, output_video: str = None,
                            scale_factor: float = 1.1, min_neighbors: int = 5,
                            min_size: Tuple[int, int] = (30, 30),
                            start_time: float = 0, end_time: float = None,
                            draw_rectangles: bool = True,
                            rectangle_color: Tuple[int, int, int] = (0, 0, 255),
                            rectangle_thickness: int = 2,
                            codec: str = "mp4v") -> List[Dict[str, Any]]:
        """Videodaki yüzleri tespit et
        
        Args:
            input_video: Giriş video dosyası yolu
            output_video: Yüz tespiti yapılmış video çıktısı (None=kaydetmez)
            scale_factor: Ölçek faktörü (opencv cascade parametresi)
            min_neighbors: Minimum komşu sayısı (opencv cascade parametresi)
            min_size: Minimum yüz boyutu (genişlik, yükseklik)
            start_time: Başlangıç zamanı (saniye)
            end_time: Bitiş zamanı (saniye) (None=videonun sonuna kadar)
            draw_rectangles: Yüz tespiti için dikdörtgen çiz
            rectangle_color: Dikdörtgen rengi (BGR formatında)
            rectangle_thickness: Dikdörtgen kalınlığı
            codec: Video codec'i
            
        Returns:
            List[Dict]: Tespit edilen yüz bilgileri
            [
                {
                    'frame': kare numarası,
                    'timestamp': zaman damgası (sn),
                    'timestamp_formatted': zaman damgası (hh:mm:ss),
                    'face_count': tespit edilen yüz sayısı,
                    'faces': [(x, y, w, h), ...] (yüz koordinatları)
                },
                ...
            ]
        """
        self._check_video_path(input_video)
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        out = None
        face_data = []
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Zaman bilgilerini kare indekslerine dönüştür
            start_frame = int(start_time * fps) if start_time > 0 else 0
            end_frame = int(end_time * fps) if end_time is not None else total_frames
            
            # Yüz tespiti için cascade classifier yükle
            face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            face_cascade = cv2.CascadeClassifier(face_cascade_path)
            
            # Çıkış video ayarları
            if output_video:
                fourcc = cv2.VideoWriter_fourcc(*codec)
                
                # Çıktı dizinini kontrol et ve oluştur
                output_dir = os.path.dirname(output_video)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # İstenen kareye atla
            if start_frame > 0:
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            
            frame_count = start_frame
            
            while frame_count < end_frame:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Yüz tespiti için gri tonlamalı görüntüye dönüştür
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Yüzleri tespit et
                faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=scale_factor,
                    minNeighbors=min_neighbors,
                    minSize=min_size
                )
                
                # Tespit edilen yüzleri kaydet
                if len(faces) > 0:
                    timestamp = frame_count / fps
                    face_info = {
                        'frame': frame_count,
                        'timestamp': timestamp,
                        'timestamp_formatted': str(datetime.timedelta(seconds=int(timestamp))),
                        'face_count': len(faces),
                        'faces': [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in faces]
                    }
                    face_data.append(face_info)
                    
                    # Yüz dikdörtgenleri çiz
                    if draw_rectangles and output_video:
                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x+w, y+h), rectangle_color, rectangle_thickness)
                
                # Çıkış videosu oluştur
                if output_video:
                    # Bilgileri ekrana yaz
                    cv2.putText(frame, f"Yüz Sayısı: {len(faces)}", 
                              (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    time_info = str(datetime.timedelta(seconds=int(frame_count/fps)))
                    cv2.putText(frame, f"Zaman: {time_info}", 
                              (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    out.write(frame)
                
                frame_count += 1
            
            return face_data
        finally:
            cap.release()
            if out is not None:
                out.release()
    
    def recognize_faces_in_video(self, input_video: str, known_faces_dir: str, 
                               output_video: str = None, tolerance: float = 0.6,
                               start_time: float = 0, end_time: float = None,
                               codec: str = "mp4v", skip_frames: int = 5) -> List[Dict[str, Any]]:
        """Videodaki yüzleri tanı
        
        Args:
            input_video: Giriş video dosyası yolu
            known_faces_dir: Bilinen yüzlerin bulunduğu klasör 
                             (her kişi için bir alt klasör, içinde o kişinin resimleri)
            output_video: Yüz tanıma yapılmış video çıktısı (None=kaydetmez)
            tolerance: Eşleşme toleransı (0-1 arası, düşük değer daha kesin eşleşme)
            start_time: Başlangıç zamanı (saniye)
            end_time: Bitiş zamanı (saniye) (None=videonun sonuna kadar)
            codec: Video codec'i
            skip_frames: Kaç karede bir işlem yapılacağı (performans için)
            
        Returns:
            List[Dict]: Tanınan yüz bilgileri
            [
                {
                    'frame': kare numarası,
                    'timestamp': zaman damgası (sn),
                    'timestamp_formatted': zaman damgası (hh:mm:ss),
                    'face_count': tespit edilen yüz sayısı,
                    'recognized_faces': [
                        {
                            'name': kişi adı,
                            'location': (x, y, w, h),
                            'confidence': güven değeri
                        },
                        ...
                    ]
                },
                ...
            ]
        """
        try:
            # face_recognition kütüphanesini yüklemeyi dene
            import face_recognition
        except ImportError:
            raise ImportError("Bu özellik için 'face_recognition' kütüphanesi gereklidir. Lütfen kurun: pip install face_recognition")
        
        self._check_video_path(input_video)
        
        # Bilinen yüzleri yükle
        known_face_encodings = []
        known_face_names = []
        
        if not os.path.exists(known_faces_dir):
            raise FileNotFoundError(f"Bilinen yüzler klasörü bulunamadı: {known_faces_dir}")
        
        # Her kişi için alt klasörleri tara
        for person_name in os.listdir(known_faces_dir):
            person_dir = os.path.join(known_faces_dir, person_name)
            if os.path.isdir(person_dir):
                # Kişiye ait görüntüleri bul
                for img_file in os.listdir(person_dir):
                    if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        img_path = os.path.join(person_dir, img_file)
                        try:
                            # Görüntüyü yükle ve yüz kodlamasını çıkar
                            image = face_recognition.load_image_file(img_path)
                            face_encodings = face_recognition.face_encodings(image)
                            
                            if len(face_encodings) > 0:
                                # İlk yüz kodlamasını kullan
                                known_face_encodings.append(face_encodings[0])
                                known_face_names.append(person_name)
                                print(f"Bilinen yüz yüklendi: {person_name} ({img_file})")
                        except Exception as e:
                            print(f"Görüntü yükleme hatası ({img_path}): {e}")
        
        if not known_face_encodings:
            raise ValueError("Hiç bilinen yüz bulunamadı. Lütfen known_faces_dir'de her kişi için bir klasör oluşturun.")
        
        print(f"Toplam {len(known_face_encodings)} bilinen yüz yüklendi, {len(set(known_face_names))} farklı kişi")
        
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise ValueError(f"{input_video} dosyası açılamadı")
        
        out = None
        recognition_data = []
        
        try:
            # Video özelliklerini al
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Zaman bilgilerini kare indekslerine dönüştür
            start_frame = int(start_time * fps) if start_time > 0 else 0
            end_frame = int(end_time * fps) if end_time is not None else total_frames
            
            # Çıkış video ayarları
            if output_video:
                fourcc = cv2.VideoWriter_fourcc(*codec)
                
                # Çıktı dizinini kontrol et ve oluştur
                output_dir = os.path.dirname(output_video)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
            
            # İstenen kareye atla
            if start_frame > 0:
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            
            frame_count = start_frame
            process_this_frame = 0  # Her skip_frames karede bir yüz tanıma işlemi yap
            
            # Son tanınan yüzleri sakla (atlanmış kareler için)
            last_face_locations = []
            last_face_names = []
            
            while frame_count < end_frame:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # BGR'den RGB'ye dönüştür (face_recognition için)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Her skip_frames karede bir yüz tanıma yap
                if process_this_frame == 0:
                    # Mevcut karedeki tüm yüzlerin konumlarını bul
                    face_locations = face_recognition.face_locations(rgb_frame)
                    
                    if face_locations:
                        # Yüz kodlamalarını çıkar
                        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                        
                        face_names = []
                        face_confidences = []
                        
                        # Her yüz kodlamasını bilinen yüzlerle karşılaştır
                        for face_encoding in face_encodings:
                            # Bilinen tüm yüzlerle karşılaştır
                            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance)
                            
                            name = "Bilinmeyen"
                            confidence = 0.0
                            
                            # En iyi eşleşmeyi bul
                            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                            if len(face_distances) > 0:
                                best_match_index = np.argmin(face_distances)
                                if matches[best_match_index]:
                                    name = known_face_names[best_match_index]
                                    # Güven değerini hesapla (düşük mesafe = yüksek güven)
                                    confidence = 1.0 - face_distances[best_match_index]
                            
                            face_names.append(name)
                            face_confidences.append(confidence)
                        
                        # Son tanınan yüzleri güncelle
                        last_face_locations = face_locations
                        last_face_names = face_names
                        
                        # Tanıma bilgilerini kaydet
                        timestamp = frame_count / fps
                        recognition_info = {
                            'frame': frame_count,
                            'timestamp': timestamp,
                            'timestamp_formatted': str(datetime.timedelta(seconds=int(timestamp))),
                            'face_count': len(face_locations),
                            'recognized_faces': [
                                {
                                    'name': name,
                                    'location': (location[3], location[0], location[1] - location[0], location[2] - location[3]),  # (x, y, w, h)
                                    'confidence': float(conf)
                                }
                                for name, conf, location in zip(face_names, face_confidences, face_locations)
                            ]
                        }
                        recognition_data.append(recognition_info)
                
                # Çıkış videosu için bilgileri ekle
                if output_video:
                    # Dikdörtgenleri ve isimleri çiz
                    for (top, right, bottom, left), name in zip(last_face_locations, last_face_names):
                        # Dikdörtgen
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                        
                        # İsim etiketi için arka plan
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                        
                        # İsim
                        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 
                                  0.8, (255, 255, 255), 1)
                    
                    # Bilgileri ekrana yaz
                    cv2.putText(frame, f"Yüz Sayısı: {len(last_face_locations)}", 
                              (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    time_info = str(datetime.timedelta(seconds=int(frame_count/fps)))
                    cv2.putText(frame, f"Zaman: {time_info}", 
                              (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    out.write(frame)
                
                # Sonraki kare için sayaçları güncelle
                process_this_frame = (process_this_frame + 1) % skip_frames
                frame_count += 1
            
            return recognition_data
        finally:
            cap.release()
            if out is not None:
                out.release()

if __name__ == "__main__":
    video_utils() 