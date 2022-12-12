class phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name=model_name
        self._price = max(price,0)
        
        def full_name(self):
            return f"{self,brand} {self.model_name}"
        def make_a_call(self,number):
            return f"calling {number}......"
        
        class smartphone(phone): #child class
            def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
                # phone.__init__(self,brand,model_name,price)
                super().__init__(brand,model_name,price)
                
                # self.brand = brand
                # self.model_name=model_name
                # self._print = max(price,0)
                self.rear_camera=rear_camera
                
                # def full_name(self):
                #     return f"{self.brand} {self.model_name}"
                # def make_a_call(self,number):
                #     return f"calling {number}...."
                phone=phone('nofia','1100',1000)
                smartphone=smartphone('oneplus','5',30000,'6GB','64GB','20MP')
                print(phone.full_name())
                print(smartphone.full_name()+ f"and price is {smartphone._price}")