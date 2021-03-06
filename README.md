# STZ-yolov5
## Параметры обучения
1.	Data set:
  + Рекомендуемое количество изображений на 1 класс начинается от 1500
  + Необходимо разнообразие изображений для реальных случаев использования по типу разного освещения, разной погоды или времен года (если объект используется на улице), разных ракурсов, разных источников (необходимо снимать объект с разных камер для полностью своего набора данных ли брать частично с интернета) и т.д.
  + Label consistency (согласованность этикеток) – все экземпляры классов должны быть помечены. При частичной маркировке могут возникнуть ошибки в обучении (например на изображении 2 ручки а помечена только одна)
  + В наборе данных нужны фоновые изображения – изображения, на которых нет объектов для обучения. Количество таких изображений не должно превышать 10% (том же COCO их около 1%). Для фоновых изображений не требуется никаких меток
2.	Epoch – обучение нейронной сети со всему обещающими данными за один цикл, поскольку для каждого набора данных количество эпох может отличаться, их лучше всего устанавливать экспериментально начиная с 300. Далее, если не происходит переобучения, их количество можно увеличить до 600, 1200 и т.д.
3.	Batch – количество обучающих выборок или примеров за одну итерацию. Чем меньше размер пакета, тем больше нужно памяти. Также маленькие размеры приводят к плохой статистике batchnorm и их следует избегать 
4.	Img – в большинстве рекомендуемых случаях используют размер который кратный 64, но выставлять слишком маленький размер не рекомендуется.
5.	Hyperparameter – при должном опыте работы с нейросетями их можно настраивать вручную под конкретную задачу, в противном случае их необходимо эволюционировать 
6.	Network Architecture – yolov5 позволяет выбрать свою архитектуру сети с вашими персональными настройками, но для начала рекомендуется использовать одну из предложенных стандартных 
7.	mAP(средняя точность) – среднее значение AP для нескольких loU(измеряет перекрытие между двумя областями, для некоторых наборов данных предопределяется некий порог например 0.5, и это используется для классификации предсказания(true/false)), для COCO AP это среднее значение по 10 уровням loU по 80 категориям от 0.5 до 0.95 с размером шага 0.05.
8.	Precision & recall
  + Precision измеряет, насколько точны ваши предсказания. Например, какой процент ваших предсказаний корректен.
  + Recall измеряет, насколько хорошо вы находите все положительные образцы. Например, мы можем находить 80% от всех возможных положительных случаев в наших К лучших предсказаниях.

## Результаты обучения
### Нормальный датасет (New normal dataset)
#### 448 px 16 batch 1200 epoch
mAP 0,5 - 0,95
![mAP 0,5 - 0,95](https://user-images.githubusercontent.com/86681516/162638155-2b163c29-e5bb-4ca7-ad90-4ca7f6ff66bc.png)

Оставшиеся графики можно найти в папке config

## Описание .py
1. main.py - не нужна, там лежат остатки от версии без гуи
2. setConstants.py - содержит функции:
+ строющую модель по полученным весам;
+ преобразующую картинку в yolov5 формат;
+ cодержит параметры:
+ input_width,input_height - размеры обрабатываемого изображения(почему-то нельзя менять)
+ colors - цвета для выделения
3. detectObject.py - содержит набор функций для обработки изображения(детекции ручки)
4. startObjectDetection.py - содержит функцию, получающую на входе изображение с веб-камеры и возвращающую обработанное изображение (с границами и названием объекта)
5. design.py - дизайн интерфейса + обработка нажатий кнопок

## GUI
### Чего получилось достичь:
- выбор весов из программы;
- автоматическое составление списка доступных камер;
- выбор из доступных камер для отображения(возможны баги, т.к. не имелось возможности тестить с двумя и более вебками);
- вывод изображения с вебки внутри программы;
- ожидание повторного подключения камеры при её отключении;
- остановка показа + повторное начало показ(не добавлено в программу, не хватило времени);
### Чего не получилось достичь:
- отключение возможности нажатия кнопок при детекции;
- подключение обработки видеокартой;
- изменение параметров детекции (вебкамера, веса) в ходе исполнения программы;
- отлов исключения, если для подключенных весов использованы не те веса;
