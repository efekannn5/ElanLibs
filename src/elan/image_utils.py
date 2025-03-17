import cv2
import numpy as np
import os

class image_utils:
    def __init__(self):
        """Görüntü işleme yardımcıları sınıfı"""
        pass

    def _read_image(self, image_input):
        """Görüntüyü oku - dosya yolu veya numpy dizisi kabul eder"""
        if isinstance(image_input, str):
            if not os.path.exists(image_input):
                raise FileNotFoundError(f"Görüntü dosyası bulunamadı: {image_input}")
            return cv2.imread(image_input)
        elif isinstance(image_input, np.ndarray):
            return image_input.copy()
        else:
            raise TypeError("Görüntü girişi bir dosya yolu (str) veya numpy dizisi olmalıdır")
    
    def _save_result(self, image, output_path=None):
        """İşlem sonucunu kaydet veya döndür"""
        if output_path:
            cv2.imwrite(output_path, image)
            return True
        return image

    def to_grayscale(self, image_input, output_path=None):
        """Görüntüyü gri tonlamaya dönüştür
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        if len(image.shape) == 2 or image.shape[2] == 1:
            gray_image = image  # Zaten gri tonlamalı
        else:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return self._save_result(gray_image, output_path)

    def resize(self, image_input, width, height, keep_aspect_ratio=False, output_path=None):
        """Görüntüyü yeniden boyutlandır
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            width: Yeni genişlik
            height: Yeni yükseklik
            keep_aspect_ratio: En boy oranını koru
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        if keep_aspect_ratio:
            h, w = image.shape[:2]
            aspect = w / h
            
            if width == 0:
                width = int(height * aspect)
            elif height == 0:
                height = int(width / aspect)
            else:
                # En boy oranını koruyarak sığdır
                new_aspect = width / height
                if new_aspect > aspect:  # Yeni oran daha geniş
                    width = int(height * aspect)
                else:  # Yeni oran daha dar
                    height = int(width / aspect)
        
        resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        return self._save_result(resized_image, output_path)

    def rotate(self, image_input, angle, output_path=None):
        """Görüntüyü döndür
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            angle: Döndürme açısı (derece)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return self._save_result(rotated_image, output_path)
    
    def crop(self, image_input, x, y, width, height, output_path=None):
        """Görüntüyü kırp
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            x, y: Başlangıç koordinatları
            width, height: Kırpma boyutları
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        cropped_image = image[y:y+height, x:x+width]
        return self._save_result(cropped_image, output_path)
    
    def add_blur(self, image_input, blur_type='gaussian', kernel_size=5, output_path=None):
        """Görüntüye bulanıklık ekle
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            blur_type: Bulanıklaştırma tipi ('gaussian', 'median', 'box')
            kernel_size: Bulanıklaştırma şiddeti (tek sayı olmalı)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        # kernel size tek sayı olmalı
        if kernel_size % 2 == 0:
            kernel_size += 1
            
        if blur_type == 'gaussian':
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        elif blur_type == 'median':
            blurred = cv2.medianBlur(image, kernel_size)
        elif blur_type == 'box':
            blurred = cv2.blur(image, (kernel_size, kernel_size))
        else:
            raise ValueError("Geçersiz blur_type. 'gaussian', 'median' veya 'box' kullanın")
            
        return self._save_result(blurred, output_path)
    
    def detect_edges(self, image_input, method='canny', threshold1=100, threshold2=200, output_path=None):
        """Görüntüdeki kenarları tespit et
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            method: Kenar tespit yöntemi ('canny', 'sobel')
            threshold1, threshold2: Canny için eşik değerleri
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        if method == 'canny':
            edges = cv2.Canny(gray, threshold1, threshold2)
        elif method == 'sobel':
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            edges = cv2.magnitude(sobelx, sobely)
            edges = np.uint8(edges)
        else:
            raise ValueError("Geçersiz method. 'canny' veya 'sobel' kullanın")
            
        return self._save_result(edges, output_path)
    
    def adjust_brightness(self, image_input, factor, output_path=None):
        """Görüntü parlaklığını ayarla
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            factor: Parlaklık faktörü (1.0 değişim yok, >1.0 daha parlak, <1.0 daha karanlık)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        # Parlaklık ayarı
        adjusted = cv2.convertScaleAbs(image, alpha=factor, beta=0)
        return self._save_result(adjusted, output_path)
    
    def adjust_contrast(self, image_input, factor, output_path=None):
        """Görüntü kontrastını ayarla
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            factor: Kontrast faktörü (1.0 değişim yok, >1.0 daha yüksek kontrast, <1.0 daha düşük kontrast)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        # Kontrast ayarı
        mean = np.mean(image)
        adjusted = cv2.convertScaleAbs(image, alpha=factor, beta=(1.0-factor) * mean)
        return self._save_result(adjusted, output_path)
    
    def equalize_histogram(self, image_input, output_path=None):
        """Görüntü histogramını eşitle (iyileştirme)
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        if len(image.shape) == 2:  # Gri tonlamalı görüntü
            equalized = cv2.equalizeHist(image)
        else:  # Renkli görüntü
            # YUV uzayına dönüştür (Y = parlaklık kanalı)
            yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            # Parlaklık kanalını eşitle
            yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
            # BGR'ye geri dönüştür
            equalized = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
            
        return self._save_result(equalized, output_path)
    
    def add_text(self, image_input, text, position, font_size=1, color=(255,255,255), thickness=2, output_path=None):
        """Görüntüye metin ekle
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            text: Eklenecek metin
            position: Metin konumu (x, y)
            font_size: Yazı tipi boyutu
            color: Metin rengi (BGR formatında tuple)
            thickness: Metin kalınlığı
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        # Metni ekle
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, position, font, font_size, color, thickness, cv2.LINE_AA)
        
        return self._save_result(image, output_path)
    
    def add_rectangle(self, image_input, top_left, bottom_right, color=(0,255,0), thickness=2, output_path=None):
        """Görüntüye dikdörtgen ekle
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            top_left: Sol üst köşe koordinatları (x, y)
            bottom_right: Sağ alt köşe koordinatları (x, y)
            color: Çizgi rengi (BGR formatında tuple)
            thickness: Çizgi kalınlığı
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        # Dikdörtgen ekle
        cv2.rectangle(image, top_left, bottom_right, color, thickness)
        
        return self._save_result(image, output_path)
    
    def detect_faces(self, image_input, method='mediapipe', draw_rectangles=True, 
                     rectangle_color=(0, 0, 255), rectangle_thickness=2, 
                     scale_factor=1.1, min_neighbors=4, min_size=(30, 30),
                     draw_landmarks=False, output_path=None):
        """Görüntüdeki yüzleri tespit et
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            method: Kullanılacak yüz algılama yöntemi ('opencv', 'dlib', 'mediapipe')
            draw_rectangles: Yüzlerin etrafına dikdörtgen çiz
            rectangle_color: Dikdörtgen rengi (B, G, R) formatında, varsayılan kırmızı
            rectangle_thickness: Dikdörtgen çizgi kalınlığı
            scale_factor: Her görüntü ölçeği için ne kadar küçülteceğini belirten faktör (sadece OpenCV için)
            min_neighbors: Yüz kabul edilmesi için gerekli komşu sayısı (sadece OpenCV için)
            min_size: Tespit edilebilecek minimum yüz boyutu (sadece OpenCV için)
            draw_landmarks: MediaPipe ile yüz hatlarını çiz (sadece method='mediapipe' için)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde (işlenmiş görüntü, yüz konumları)
        """
        try:
            image = self._read_image(image_input)
            original_image = image.copy()
            
            # Yüz tespiti için kullanılacak yöntemi seç
            try:
                # Varsayılan ve en iyi yöntem olarak MediaPipe'ı dene
                if method == 'mediapipe' or method not in ['opencv', 'dlib', 'mediapipe']:
                    try:
                        import mediapipe as mp
                        # MediaPipe Face Detection modülünü başlat
                        mp_face_detection = mp.solutions.face_detection
                        mp_drawing = mp.solutions.drawing_utils
                        
                        # RGB'ye dönüştür (MediaPipe RGB formatını kullanır)
                        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        
                        with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
                            results = face_detection.process(rgb_image)
                            
                            faces = []
                            if results.detections:
                                for detection in results.detections:
                                    bboxC = detection.location_data.relative_bounding_box
                                    ih, iw, _ = image.shape
                                    x, y = int(bboxC.xmin * iw), int(bboxC.ymin * ih)
                                    w, h = int(bboxC.width * iw), int(bboxC.height * ih)
                                    faces.append((x, y, w, h))
                                    
                                    if draw_rectangles:
                                        cv2.rectangle(image, (x, y), (x+w, y+h), rectangle_color, rectangle_thickness)
                                        confidence = round(detection.score[0] * 100)
                                        cv2.putText(image, f"Yüz {confidence}%", (x, y-10), 
                                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, rectangle_color, 1, cv2.LINE_AA)
                                    
                                    # Yüz hatlarını çiz (isteğe bağlı)
                                    if draw_landmarks:
                                        mp_drawing.draw_detection(image, detection)
                    except (ImportError, Exception) as e:
                        print(f"MediaPipe kullanılamadı, alternatif yönteme geçiliyor: {e}")
                        # MediaPipe yüklenemezse veya hata verirse face_recognition'a geçiş yap
                        method = 'dlib'
                
                # Face Recognition (DLIB) ile yüz algılama dene
                if method == 'dlib':
                    try:
                        # Önce dlib'i kontrol edelim
                        try:
                            import dlib
                        except ImportError:
                            raise ImportError("'dlib' kütüphanesi yüklenemedi. Kurulum için: pip install dlib>=19.22.0")
                            
                        # Şimdi face_recognition'ı kullanalım
                        import face_recognition
                        # RGB'ye dönüştür (face_recognition kütüphanesi RGB formatını kullanır)
                        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        
                        # Yüz konumlarını tespit et
                        face_locations = face_recognition.face_locations(rgb_image)
                        faces = [(left, top, right - left, bottom - top) 
                                for (top, right, bottom, left) in face_locations]
                        
                        if draw_rectangles and face_locations:
                            for (top, right, bottom, left) in face_locations:
                                cv2.rectangle(image, (left, top), (right, bottom), rectangle_color, rectangle_thickness)
                                cv2.putText(image, f"Yüz", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 
                                            0.5, rectangle_color, 1, cv2.LINE_AA)
                    except (ImportError, Exception) as e:
                        print(f"DLIB/face_recognition kullanılamadı, OpenCV'ye geçiliyor: {e}")
                        # Face Recognition yüklenemezse veya hata verirse OpenCV'ye geçiş yap
                        method = 'opencv'
                
                # OpenCV ile yüz algılama (son çare olarak kullan)
                if method == 'opencv':
                    faces = self._detect_faces_opencv(image, scale_factor, min_neighbors, min_size)
                    
                    if draw_rectangles and len(faces) > 0:
                        for (x, y, w, h) in faces:
                            cv2.rectangle(image, (x, y), (x+w, y+h), rectangle_color, rectangle_thickness)
                            cv2.putText(image, f"Yüz", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                                        0.5, rectangle_color, 1, cv2.LINE_AA)
                
            except Exception as e:
                print(f"Yüz algılama hatası: {e}")
                # Hiçbir yöntem çalışmazsa boş sonuç döndür
                faces = []
            
            if output_path:
                cv2.imwrite(output_path, image)
                return faces
            else:
                return image, faces
                
        except Exception as e:
            print(f"Görüntü işleme hatası: {e}")
            # Ciddi bir hata olursa orijinal görüntüyü ve boş liste döndür
            return image_input if isinstance(image_input, np.ndarray) else np.zeros((100, 100, 3), dtype=np.uint8), []
    
    def _detect_faces_opencv(self, image, scale_factor=1.1, min_neighbors=4, min_size=(30, 30)):
        """OpenCV ile yüz tespiti yapar"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Haar Cascade sınıflandırıcısını yükle
        face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        
        # Daha güvenilir bir tespit için, önceden LBP sınıflandırıcısı ile daraltılmış bölgeyi tara
        eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        
        # Yüzleri tespit et
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=scale_factor, 
            minNeighbors=min_neighbors,
            minSize=min_size
        )
        
        # Daha doğru tespitler için göz kontrolü yapabiliriz
        verified_faces = []
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) >= 1:  # En az bir göz tespit edilirse
                verified_faces.append((x, y, w, h))
        
        return verified_faces if verified_faces else faces
    
    def recognize_faces(self, image_input, known_faces_dir, tolerance=0.6, 
                       draw_labels=True, label_color=(0, 255, 0), output_path=None):
        """Yüzleri tanı ve isimlendir
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            known_faces_dir: Bilinen yüzler klasörü (Her kişi için ayrı bir klasör)
            tolerance: Eşleşme eşiği (düşük değer = daha kesin eşleşme)
            draw_labels: Tanınan yüzlere isim etiketi çiz
            label_color: Etiket rengi (B, G, R) formatında
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde (işlenmiş görüntü, tanıma sonuçları)
        """
        # Önce dlib'i kontrol edelim
        try:
            import dlib
        except ImportError:
            raise ImportError("'dlib' kütüphanesi yüklenemedi. Kurulum için: pip install dlib>=19.22.0")
            
        # Şimdi face_recognition'ı yükleyelim
        try:
            import face_recognition
            import os
        except ImportError:
            raise ImportError("Bu fonksiyon için 'face_recognition' kütüphanesi gereklidir. "
                             "Yüklemek için: pip install face_recognition>=1.3.0")
        
        try:
            image = self._read_image(image_input)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Bilinen yüzleri yükle
            known_face_encodings = []
            known_face_names = []
            
            if not os.path.exists(known_faces_dir):
                raise FileNotFoundError(f"Bilinen yüzler klasörü bulunamadı: {known_faces_dir}")
            
            person_count = 0
            for person_name in os.listdir(known_faces_dir):
                person_dir = os.path.join(known_faces_dir, person_name)
                if os.path.isdir(person_dir):
                    person_count += 1
                    image_count = 0
                    for image_name in os.listdir(person_dir):
                        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                            image_count += 1
                            image_path = os.path.join(person_dir, image_name)
                            face_image = face_recognition.load_image_file(image_path)
                            try:
                                face_encoding = face_recognition.face_encodings(face_image)[0]
                                known_face_encodings.append(face_encoding)
                                known_face_names.append(person_name)
                            except IndexError:
                                print(f"Uyarı: {image_path} dosyasında yüz bulunamadı, atlanıyor.")
            
            if person_count == 0:
                print(f"Uyarı: {known_faces_dir} klasöründe hiçbir kişi bulunamadı.")
                
            if not known_face_encodings:
                raise ValueError(f"Bilinen yüz veritabanında hiçbir yüz bulunamadı. Lütfen {known_faces_dir} dizinini kontrol edin.")
                
            print(f"Bilgi: {len(known_face_encodings)} yüz, {person_count} kişi veritabanından yüklendi.")
            
            # Test görüntüsündeki yüzleri tespit et
            face_locations = face_recognition.face_locations(rgb_image)
            
            if not face_locations:
                print(f"Uyarı: Verilen görüntüde hiçbir yüz tespit edilemedi.")
                if output_path:
                    cv2.imwrite(output_path, image)
                    return []
                else:
                    return image, []
            
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
            
            # Tanıma sonuçlarını sakla
            face_names = []
            recognition_results = []
            
            for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                # Bilinen yüzlerle karşılaştır
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
                name = "Bilinmeyen"
                confidence = 0.0
                
                # En iyi eşleşmeyi bul
                if True in matches:
                    # Eşleşen tüm yüzleri bul
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        confidence = 1.0 - face_distances[best_match_index]
                
                face_names.append(name)
                recognition_results.append({
                    'name': name,
                    'location': (left, top, right - left, bottom - top),
                    'confidence': confidence
                })
                
                if draw_labels:
                    # Yüz etrafına dikdörtgen ve etiket çiz
                    cv2.rectangle(image, (left, top), (right, bottom), label_color, 2)
                    confidence_text = f"{confidence:.2f}" if confidence > 0 else ""
                    label = f"{name} {confidence_text}"
                    y = top - 10 if top - 10 > 10 else top + 10
                    cv2.putText(image, label, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 
                               0.5, label_color, 1, cv2.LINE_AA)
            
            if output_path:
                cv2.imwrite(output_path, image)
                return recognition_results
            else:
                return image, recognition_results
                
        except Exception as e:
            print(f"Yüz tanıma hatası: {e}")
            # Hata olursa orijinal görüntüyü ve boş sonuç döndür
            if output_path:
                try:
                    original_image = self._read_image(image_input)
                    cv2.imwrite(output_path, original_image)
                except:
                    pass
                return []
            else:
                return image_input if isinstance(image_input, np.ndarray) else np.zeros((100, 100, 3), dtype=np.uint8), []
    
    def apply_filter(self, image_input, filter_type, output_path=None):
        """Görüntüye filtre uygula
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            filter_type: Filtre tipi ('sepia', 'negative', 'sketch', 'cartoon')
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image = self._read_image(image_input)
        
        if filter_type == 'sepia':
            # Sepya filtresi
            sepia_kernel = np.array([
                [0.272, 0.534, 0.131],
                [0.349, 0.686, 0.168],
                [0.393, 0.769, 0.189]
            ])
            filtered = cv2.transform(image, sepia_kernel)
        
        elif filter_type == 'negative':
            # Negatif filtresi
            filtered = cv2.bitwise_not(image)
        
        elif filter_type == 'sketch':
            # Karakalem efekti
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inv_gray = 255 - gray
            blurred = cv2.GaussianBlur(inv_gray, (21, 21), 0)
            inv_blurred = 255 - blurred
            filtered = cv2.divide(gray, inv_blurred, scale=256.0)
        
        elif filter_type == 'cartoon':
            # Karikatür efekti
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(image, 9, 300, 300)
            filtered = cv2.bitwise_and(color, color, mask=edges)
        
        else:
            raise ValueError("Geçersiz filter_type. 'sepia', 'negative', 'sketch' veya 'cartoon' kullanın")
        
        return self._save_result(filtered, output_path)
    
    def merge_images(self, image1_input, image2_input, weight1=0.5, weight2=0.5, output_path=None):
        """İki görüntüyü karıştır
        
        Args:
            image1_input: Birinci görüntü dosya yolu veya numpy dizisi
            image2_input: İkinci görüntü dosya yolu veya numpy dizisi
            weight1: Birinci görüntü ağırlığı (0.0-1.0)
            weight2: İkinci görüntü ağırlığı (0.0-1.0)
            output_path: Sonucu kaydetmek için dosya yolu (opsiyonel)
            
        Returns:
            output_path verilmişse True, aksi halde işlenmiş görüntü
        """
        image1 = self._read_image(image1_input)
        image2 = self._read_image(image2_input)
        
        # Görüntüleri aynı boyuta getir
        h1, w1 = image1.shape[:2]
        h2, w2 = image2.shape[:2]
        
        if h1 != h2 or w1 != w2:
            image2 = cv2.resize(image2, (w1, h1))
        
        # Görüntüleri karıştır
        merged = cv2.addWeighted(image1, weight1, image2, weight2, 0)
        
        return self._save_result(merged, output_path)
    
    def save_image(self, image_input, output_path):
        """Görüntüyü kaydet
        
        Args:
            image_input: Görüntü dosya yolu veya numpy dizisi
            output_path: Kaydedilecek dosya yolu
            
        Returns:
            bool: Başarı durumu
        """
        image = self._read_image(image_input)
        return cv2.imwrite(output_path, image)

if __name__ == "__main__":
    image_utils() 