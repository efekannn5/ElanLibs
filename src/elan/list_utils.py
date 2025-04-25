class list_utils:
    def __init__(self):
        pass

    def reverse(self, input_list):
        return input_list[::-1]
    
    # Türkçe alternatif
    def tersine_cevir(self, input_list):
        return self.reverse(input_list)
    
    def sort(self, input_list):
        return sorted(input_list)
    
    # Türkçe alternatif
    def sirala(self, input_list):
        return self.sort(input_list)
      
    def unique(self, input_list):
        return list(set(input_list))
    
    # Türkçe alternatif
    def benzersiz(self, input_list):
        return self.unique(input_list)
    
if __name__ == "__main__":
    list_utils()
    

