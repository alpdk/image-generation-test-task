# Image generation test task

## Task completion time

The total time spent was approximately 8–9 hours, broken down as follows:

1) 6 hours for the text and image generation tasks
2) 2–3 hours for the testing seed impact task

## How to use repository

This repository contain 2 scripts: `main.py` and  `seed_impact.py`. 

The first script generates a furniture description from an image in the `images/furniture` directory. 
From the generated furniture description and a room description from the `room_description` directory will be generated
image of the room.

The second script checking how many time model generate unique outputs with different seeds and temperature. 
For that script repeat steps from the first script and check amount of unique outputs.

Scripts requires next arguments:
1) Seed number
2) Temperature [0.0, 2.0]
3) Model name (this repository works with gemini models)
4) API key (for the gemini models)
5) Name of the furniture image file
6) Name of the description text file

Examples:

```python
python main.py 42 2.0 gemini-2.0-flash-exp YOUR_API_KEY test.jpg test.txt
```

```python
python seed_impact.py 42 2.0 gemini-2.0-flash-exp YOUR_API_KEY test.jpg test.txt
```

## Example:

### Inputs
```text
Комната просторная и светлая, с большими окнами, через которые мягко проникает дневной свет.
Стены окрашены в теплый бежевый оттенок, создающий ощущение уюта и покоя.
В центре стоит уютный диван цвета серого льна, напротив которого размещён низкий кофейный столик из светлого дерева.
У одной стены — открытые полки с книгами, растениями в глиняных горшках и небольшими декоративными элементами.
Пол выложен светлым паркетом, частично закрытым мягким ковром в нейтральной гамме.
Потолок украшает лаконичная люстра с мягким рассеянным светом, создающим атмосферу расслабленности.
В углу — рабочий стол с ноутбуком и настольной лампой, рядом — кресло с пледом, идеальное место для чтения.
```

![test.jpg](images/furniture/test.jpg)

### Ourputs

```text
Мебель, изображенная на картинке, имеет современный, функциональный дизайн. Это, вероятно, столик для ноутбука или рабочий стол на колесах. Он отличается своей простотой, минимализмом и мобильностью.

Вот ключевые особенности стиля и дизайна:

*   **Функциональность:** Конструкция разработана с учетом практичности, чтобы ее можно было легко перемещать и использовать в разных местах. Несколько регулируемых секций обеспечивают гибкость в настройке.
*   **Материалы:** Предположительно, стол сделан из комбинации металла (для рамы и опор) и искусственных материалов (столешницы), часто это плита МДФ или ламинированное ДСП.
*   **Цвет:** Доминирует черный цвет, что придает мебели строгий и современный вид.
*   **Простота и минимализм:** Геометричные формы, прямые линии и отсутствие декоративных элементов. Конструкция сосредоточена на основной функции - обеспечить рабочую поверхность.
*   **Колеса:** Наличие колес добавляет мобильности, позволяя легко перемещать стол по комнате.
*   **Универсальность:** Дизайн позволяет использовать его как для работы с ноутбуком, так и для других целей, например, как подставку для чтения.
* **Регулируемость** Наличие подъемных механизмов делает конструкцию еще более функциональной.
В целом, мебель отражает современный стиль, акцентируя внимание на практичности, мобильности и минимализме.
```

![test.jpg](images/generated/test.jpg)

## Results

As a result of testing gemini-2.0-flash-exp is very deterministic. 
Every seed generate from 2 to 5 unique furniture descriptions, and from 5 to 8 unique room images.
Raising temperature to maximum (2.0) that makes model more creative and less predictable have a small effect on the generation.

This result are not very reliable, because there was a small amount of test due to the restrictions from gemini with free plan, 
that do not allow to make more than 10 image generation requests per minute.
