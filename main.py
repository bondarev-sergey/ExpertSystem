import tkinter as tk
from collections import Counter

MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]



LEG_AREAS = ["Передняя область бедра", "Задняя область бедра", "Голень"]
ARM_AREAS = ["Бицепс", "Трицепс", "Плечо", "Дельта"]
TORSO_AREAS = ["Задняя", "Передняя"]
PART_OF_THE_BACK = ["Трапеции", "Поясница", "Верх спины"]
AREAS_OF_THE_FRONT_PART_OF_THE_TRUNK = ["Грудные", "Пресс"]

LOWER_BODY_AREAS = ["Ягодицы", "Ноги"]
TYPES_OF_COMPLEX_EXERCISE = ["Динамическое", "Статическое"]
UPPER_BODY_AREAS = ["Руки", "Туловище"]

BODY_AREAS = {"Нижняя" : "Область нижней части тела",
            "Верхняя и нижняя" : "Вид комплексного упражнения",
            "Верхняя" : "Область верхней части тела"}

PART_BODY_AREAS = {"Ягодицы" : "Ягодицы тренировать изолированно",
                    "Ноги" : "Область ноги", 
                    "Статическое" : "С упором на пресс",
                    "Динамическое" : "С упором на спину",
                    "Руки" : "Область руки",
                    "Туловище" : "Область туловища"}

TRAINING_TYPES = {"Разгибание бедра на четвереньках" : 0.0,
                    "Приседания" : 0.0,
                    "Разгибание ног, выпады с отягощением" : 0.0,
                    "Гиперэкстензия" : 0.0,
                    "Подъемы на носки стоя" : 0.0,
                    "Планка" : 0.0,
                    "Стульчик" : 0.0,
                    "Приседания с отягощением" : 0.0,
                    "Становая тяга" : 0.0,
                    "Подъем на бицепс стоя" : 0.0,
                    "Отжимания на брусьях" : 0.0,
                    "Махи гантелями в стороны" : 0.0,
                    "Вис на перекладине, сгибания и разгибания запястий" : 0.0,
                    "Шраги с отягощением" : 0.0,
                    "Подтягивания" : 0.0,
                    "Жим гантелей лежа" : 0.0,
                    "Наклоны в бок, боковая планка" : 0.0,
                    "Скручивания" : 0.0}

def get_results():
        TRAINING_TYPES["Разгибание бедра на четвереньках"] /= 3
        TRAINING_TYPES["Гиперэкстензия"] /= 3
        TRAINING_TYPES["Приседания"] /= 3
        TRAINING_TYPES["Разгибание ног, выпады с отягощением"] /= 3
        TRAINING_TYPES["Подъемы на носки стоя"] /= 3
        TRAINING_TYPES["Планка"] /= 3
        TRAINING_TYPES["Стульчик"] /= 3
        TRAINING_TYPES["Приседания с отягощением"] /= 3
        TRAINING_TYPES["Становая тяга"] /= 3
        TRAINING_TYPES["Подъем на бицепс стоя"] /= 5
        TRAINING_TYPES["Отжимания на брусьях"] /= 5
        TRAINING_TYPES["Махи гантелями в стороны"] /= 5
        TRAINING_TYPES["Вис на перекладине, сгибания и разгибания запястий"] /= 5
        TRAINING_TYPES["Шраги с отягощением"] /= 5
        TRAINING_TYPES["Подтягивания"] /= 5
        TRAINING_TYPES["Жим гантелей лежа"] /= 5
        TRAINING_TYPES["Наклоны в бок, боковая планка"] /= 5
        TRAINING_TYPES["Скручивания"] /= 5
        c = Counter(TRAINING_TYPES)
        return c.most_common(3)[::-1]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(text="Часть тела")
        self.list_body_areas = tk.Listbox(self)
        self.list_body_areas.insert(0, *BODY_AREAS.keys())
        self.next_btn = tk.Button(self, text="Далее",
                                   command=self.after_body_area_selection)   

        self.label.grid(row=0, column=0)
        self.list_body_areas.grid(row=1, column=0)
        self.next_btn.grid(row=2, column=0) 

    def after_body_area_selection(self):
        if self.list_body_areas.curselection() is not None:
            i = self.list_body_areas.curselection()[0]
            body_area = self.list_body_areas.get(i)
            self.label_chapter = tk.Label(text=BODY_AREAS[body_area])
            self.list_part_body_areas = tk.Listbox(self)
            if BODY_AREAS[body_area] == "Область нижней части тела":
                self.list_part_body_areas.insert(0, *LOWER_BODY_AREAS)
                TRAINING_TYPES["Подъемы на носки стоя"] += 1
                TRAINING_TYPES["Разгибание бедра на четвереньках"] += 1
                TRAINING_TYPES["Приседания"] += 1
                TRAINING_TYPES["Гиперэкстензия"] += 1
                TRAINING_TYPES["Разгибание ног, выпады с отягощением"] += 1
            if BODY_AREAS[body_area] == "Вид комплексного упражнения":
                self.list_part_body_areas.insert(0, *TYPES_OF_COMPLEX_EXERCISE)
                TRAINING_TYPES["Планка"] += 1
                TRAINING_TYPES["Стульчик"] += 1
                TRAINING_TYPES["Приседания с отягощением"] += 1
                TRAINING_TYPES["Становая тяга"] += 1
            if BODY_AREAS[body_area] == "Область верхней части тела":
                self.list_part_body_areas.insert(0, *UPPER_BODY_AREAS)
                TRAINING_TYPES["Подъем на бицепс стоя"] += 1
                TRAINING_TYPES["Отжимания на брусьях"] += 1
                TRAINING_TYPES["Махи гантелями в стороны"] += 1
                TRAINING_TYPES["Вис на перекладине, сгибания и разгибания запястий"] += 1
                TRAINING_TYPES["Шраги с отягощением"] += 1
                TRAINING_TYPES["Гиперэкстензия"] += 1
                TRAINING_TYPES["Подтягивания"] += 1
                TRAINING_TYPES["Жим гантелей лежа"] += 1
                TRAINING_TYPES["Наклоны в бок, боковая планка"] += 1
                TRAINING_TYPES["Скручивания"] += 1
            self.next2_btn = tk.Button(self, text="Далее",
                                    command=self.after_training_kind_selection)
            
            self.label_chapter.grid(row=0, column=1)
            self.list_part_body_areas.grid(row=1, column=1)
            self.next2_btn.grid(row=2, column=1)
            


    def after_training_kind_selection(self):
        if self.list_part_body_areas.curselection() is not None:
            i = self.list_part_body_areas.curselection()[0]
            part_body_area = self.list_part_body_areas.get(i)
            title = PART_BODY_AREAS[part_body_area]
            self.label_kind = tk.Label(text=title)
            self.list_type_training = tk.Listbox(self)
            if PART_BODY_AREAS[part_body_area] == "Ягодицы тренировать изолированно":
                self.list_type_training.insert(0, *("Да", "Нет"))
                TRAINING_TYPES["Разгибание бедра на четвереньках"] += 1
                TRAINING_TYPES["Приседания"] += 1
            if PART_BODY_AREAS[part_body_area] == "Область ноги":
                self.list_type_training.insert(0, *LEG_AREAS)
                TRAINING_TYPES["Разгибание ног, выпады с отягощением"] += 1
                TRAINING_TYPES["Гиперэкстензия"] += 1
                TRAINING_TYPES["Подъемы на носки стоя"] += 1
            if PART_BODY_AREAS[part_body_area] == "С упором на пресс":
                TRAINING_TYPES["Планка"] += 1
                TRAINING_TYPES["Стульчик"] += 1
                self.list_type_training.insert(0, *("Да", "Нет"))
            if PART_BODY_AREAS[part_body_area] == "С упором на спину":
                self.list_type_training.insert(0, *("Да", "Нет"))
                TRAINING_TYPES["Приседания с отягощением"] += 1
                TRAINING_TYPES["Становая тяга"] += 1
            if PART_BODY_AREAS[part_body_area] == "Область руки":
                self.list_type_training.insert(0, *ARM_AREAS)
                TRAINING_TYPES["Подъем на бицепс стоя"] += 1
                TRAINING_TYPES["Отжимания на брусьях"] += 1
                TRAINING_TYPES["Махи гантелями в стороны"] += 1
                TRAINING_TYPES["Вис на перекладине, сгибания и разгибания запястий"] += 1
            if PART_BODY_AREAS[part_body_area] == "Область туловища":
                self.list_type_training.insert(0, *TORSO_AREAS)
                TRAINING_TYPES["Шраги с отягощением"] += 1
                TRAINING_TYPES["Гиперэкстензия"] += 1
                TRAINING_TYPES["Подтягивания"] += 1
                TRAINING_TYPES["Жим гантелей лежа"] += 1
                TRAINING_TYPES["Наклоны в бок, боковая планка"] += 1
                TRAINING_TYPES["Скручивания"] += 1
            self.next3_btn = tk.Button(self, text="Далее",
                command=lambda: self.after_training_type_selection(title))

            self.label_kind.grid(row=0, column=2)
            self.list_type_training.grid(row=1, column=2)
            self.next3_btn.grid(row=2, column=2)
    
    def after_training_type_selection(self, title):
        if self.list_type_training.curselection() is not None:
            i = self.list_type_training.curselection()[0]
            training_type = self.list_type_training.get(i)
            if training_type != "Задняя" and training_type != "Передняя":
                self.label_type = tk.Label(text="Тип тренировки")
                self.label_res = tk.Label()
                if title == "Ягодицы тренировать изолированно":
                    if training_type == "Да":
                        self.label_res['text'] = "Разгибание бедра на четвереньках"
                        TRAINING_TYPES["Разгибание бедра на четвереньках"] += 1
                    elif training_type == "Нет":
                        self.label_res['text'] = "Приседания"
                        TRAINING_TYPES["Приседания"] += 1
                if title == "С упором на пресс":
                    if training_type == "Да":
                        self.label_res['text'] = "Планка"
                        TRAINING_TYPES["Планка"] += 1
                    elif training_type == "Нет":
                        self.label_res['text'] = "Стульчик"
                        TRAINING_TYPES["Стульчик"] += 1
                if title == "С упором на спину":
                    if training_type == "Да":
                        self.label_res['text'] = "Становая тяга"
                        TRAINING_TYPES["Становая тяга"] += 1
                    elif training_type == "Нет":
                        self.label_res['text'] = "Приседания с отягощением"
                        TRAINING_TYPES["Приседания с отягощением"] += 1
                if training_type == "Передняя область бедра":
                    self.label_res['text'] = "Разгибание ног, выпады с отягощением"
                    TRAINING_TYPES["Разгибание ног, выпады с отягощением"] += 1
                if training_type == "Задняя область бедра":
                    self.label_res['text'] = "Гиперэкстензия"
                    TRAINING_TYPES["Гиперэкстензия"] += 1
                if training_type == "Голень":
                    self.label_res['text'] = "Подъемы на носки стоя"
                    TRAINING_TYPES["Подъемы на носки стоя"] += 1
                if training_type == "Бицепс":
                    self.label_res['text'] = "Подъем на бицепс стоя"
                    TRAINING_TYPES["Подъем на бицепс стоя"] += 1
                if training_type == "Трицепс":
                    self.label_res['text'] = "Отжимания на брусьях"
                    TRAINING_TYPES["Отжимания на брусьях"] += 1
                if training_type == "Плечо":
                    self.label_res['text'] = "Махи гантелями в стороны"
                    TRAINING_TYPES["Махи гантелями в стороны"] += 1
                if training_type == "Дельта":
                    self.label_res['text'] = "Вис на перекладине, сгибания и разгибания запястий"
                    TRAINING_TYPES["Вис на перекладине, сгибания и разгибания запястий"] += 1

                self.label_type.grid(row=3, column=0)
                self.label_res.grid(row=4, column=0)

                maximums = get_results()
                s = ""
                for i in range(3):
                    s += maximums[i][0] + ": " + str(maximums[i][1]) + "\n"
                self.label_info = tk.Label(text=s)
                self.label_info.grid(row=5, column=0, columnspan=2, sticky=tk.W)


            else:
                if training_type == "Задняя":
                    self.label_subtype = tk.Label(text="Часть спины")
                    self.list_subtype_training = tk.Listbox(self)
                    self.list_subtype_training.insert(0, *("Трапеции", "Поясница", "Верх спины"))
                    TRAINING_TYPES["Шраги с отягощением"] += 1
                    TRAINING_TYPES["Гиперэкстензия"] += 1
                    TRAINING_TYPES["Подтягивания"] += 1
                if training_type == "Передняя":
                    self.label_subtype = tk.Label(text="Область передней части туловища")
                    self.list_subtype_training = tk.Listbox(self)
                    self.list_subtype_training.insert(0, *("Грудные", "Пресс"))
                    TRAINING_TYPES["Жим гантелей лежа"] += 1
                    TRAINING_TYPES["Наклоны в бок, боковая планка"] += 1
                    TRAINING_TYPES["Скручивания"] += 1
                self.label_subtype.grid(row=0, column=3)
                self.list_subtype_training.grid(row=1, column=3)
                self.next4_btn = tk.Button(self, text="Далее",
                    command=self.after_training_subtype_selection)
                self.next4_btn.grid(row=2, column=3)
                    
    def after_training_subtype_selection(self):
        if self.list_subtype_training.curselection() is not None:
            i = self.list_subtype_training.curselection()[0]
            training_subtype = self.list_subtype_training.get(i)
            if training_subtype != "Пресс":
                self.label_type = tk.Label(text="Тип тренировки")
                self.label_res = tk.Label()
                if training_subtype == "Трапеции":
                    self.label_res['text'] = "Шраги с отягощением"
                    TRAINING_TYPES["Шраги с отягощением"] += 1
                if training_subtype == "Поясница":
                    self.label_res['text'] = "Гиперэкстензия"
                    TRAINING_TYPES["Гиперэкстензия"] += 1
                if training_subtype == "Верх спины":
                    self.label_res['text'] = "Подтягивания"
                    TRAINING_TYPES["Подтягивания"] += 1
                if training_subtype == "Грудные":
                    self.label_res['text'] = "Жим гантелей лежа"
                    TRAINING_TYPES["Жим гантелей лежа"] += 1

                self.label_type.grid(row=3, column=0)
                self.label_res.grid(row=4, column=0)

                maximums = get_results()
                s = ""
                for i in range(3):
                    s += maximums[i][0] + ": " + str(maximums[i][1]) + "\n"
                self.label_info = tk.Label(text=s)
                self.label_info.grid(row=5, column=0, columnspan=2, sticky=tk.W)
            else:
                self.label_specific = tk.Label(text="Тренировать дополнительно косые мышцы")
                self.list_specific = tk.Listbox(self)
                self.list_specific.insert(0, *("Да", "Нет"))
                TRAINING_TYPES["Наклоны в бок, боковая планка"] += 1
                TRAINING_TYPES["Скручивания"] += 1
                self.label_specific.grid(row=0, column=4)
                self.list_specific.grid(row=1, column=4)
                self.next5_btn = tk.Button(self, text="Далее",
                    command=self.after_specific_selection)
                self.next5_btn.grid(row=2, column=4)

    def after_specific_selection(self):
        if self.list_specific.curselection() is not None:
            i = self.list_specific.curselection()[0]
            specific = self.list_specific.get(i)
            self.label_type = tk.Label(text="Тип тренировки")
            self.label_res = tk.Label()
            if specific == "Да":
                self.label_res['text'] = "Наклоны в бок, боковая планка"
                TRAINING_TYPES["Наклоны в бок, боковая планка"] += 1
            else:
                self.label_res['text'] = "Скручивания"
                TRAINING_TYPES["Скручивания"] += 1

            self.label_type.grid(row=3, column=0)
            self.label_res.grid(row=4, column=0)

            maximums = get_results()
            s = ""
            for i in range(3):
                s += maximums[i][0] + ": " + str(maximums[i][1]) + "\n"
            self.label_info = tk.Label(text=s)
            self.label_info.grid(row=5, column=0, columnspan=2, sticky=tk.W)
                
                        

if __name__ == "__main__":
    app = App()
    app.mainloop()