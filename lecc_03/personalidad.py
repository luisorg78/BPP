class personalidad:
    '''Esta clase se va a adentrar en la psicología del personaje
    a desarrollar.
    Atributos
    ---------
    nombre:
        El nombre del personaje
    Estado civil:
        Si está casado o sigue siendo feliz
    Estado mental:
        Como de pirado está
    Terapias:
        Número de terapias recibidas
        
    Métodos
    -------
    quejarse:
        En función de su estado mental se quejará más o menos
    terapia:
        En función de su estado civil y su estado mental se le 
        asignará una terapia
    alta:
        Se determinará si está en condiciones de recibir el alta
       
    ejemplo
    _______
    >>>paciente1=personalidad("manolo","tarado","soltero",0)
    >>>print(paciente1.terapia())
    >>>print(paciente1.alta())
    
    '''
    def __init__(self,nombre,est_civil,est_mental,terapias):
        self.nombre=nombre
        self.est_civil=est_civil
        self.est_mental=est_mental
        self.terapias=terapias
    
    def quejarse(self):
        '''
        Si el hombre no está sano, se quejará mucho
        '''
        if self.est_civil!="Soltero":
            return "¡quién me mandaría a mi!"
        elif self.est_mental!="Sano":
            return "¡veo burros volando"
        else:
            return "¡soy normalito!"
    
    def terapia(self):
        '''
        Si la persona está sana y soltera, no recibirá terapia.
        En el resto de los casos sí 
        '''
        if self.est_mental=="sano" and self.est_civil=="soltero":
            return "No necesitas terapia de momento"
        else:
            return "Pasa por aquella puerta por favor"
    def alta(self):
        '''
        En función del estado civil y mental, necesitará un determinado
        número de terapias para recibir el alta.
        '''
        if self.est_mental!="sano" and self.est_civil!="soltero":
            if self.terapias>5:
                return "Tiene usted el alta"
            else:
                return "Vuelva la semana que viene"
        elif self.est_civil!="soltero":
            if self.terapias>3:
                return "Tiene usted el alta"
            else:
                return "Vuelva la semana que viene"
        elif self.est_mental!="soltero":
            if self.terapias>2:
                return "Tiene usted el alta"
            else:
                return "Vuelva la semana que viene"
        else:
            return "Tiene usted el alta"


paciente1=personalidad("manolo","tarado","soltero",0)
print(paciente1.terapia())
print(paciente1.alta())



   
    