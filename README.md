# STZ-yolov5
### Параметры обучения
1.	Data set:
  •	Рекомендуемое количество изображений на 1 класс начинается от 1500
  •	Необходимо разнообразие изображений для реальных случаев использования по типу разного освещения, разной погоды или времен года (если объект используется на улице), разных ракурсов, разных источников (необходимо снимать объект с разных камер для полностью своего набора данных ли брать частично с интернета) и т.д.
  •	Label consistency (согласованность этикеток) – все экземпляры классов должны быть помечены при частичной маркировке могут возникнуть ошибки в обучении (например на изображении 2 ручки а помечена только одна)
  •	Точность маркировки при разметке изображений метки должны полностью охватывать каждый объект между объектом и его размеченной рамкой не должно существовать пространства, а также не должно быть не размеченных изображений с нужными объектами 
  •	Также в наборе данных нужны фоновые изображения – изображения, на которых нет объектов для обучения количество таких изображений не должно превышать 10% в том же COCO их около 1% для фоновых изображений не требуется никаких меток

2.	Epoch – обучение нейронной сети со всему обещающими данными за один цикл, поскольку для каждого набора данных количество эпох может отличаться, их лучше всего устанавливать экспериментально начиная с 300 далее если не происходит переобучения их количество можно увеличить до 600, 1200 и т.д.
3.	Batch – количество обучающих выборок или примеров за одну итерацию. Чем меньше размер пакета, тем больше нужно памяти. Также  маленькие размеры приводят к плохой статистике batchnorm и их следует избегать 
4.	Img – в большинстве рекомендуемых случаях используют размер который кратный 64, но выставлять слишком маленький размер не рекомендуется в том же COCO используется 640, хотя из-за большого количества мелких объектов его можно увеличить до 1280.
5.	Hyperparameter – при должном опыте работы с нейросетями их можно настраивать вручную под конкретную задачу в противном случае их необходимо эволюционировать 
6.	Network Architecture- yolov5 позволяет выбрать свою архитектуру сети с вашими персональными настройками, но для начала рекомендуется использовать одну из предложенных стандартных 

