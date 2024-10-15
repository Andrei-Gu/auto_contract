# Auto contract

В небольшом автопарке имелась потребность в ускорении создания документов: договоры продажи и аренды автомобилей, доверенностей в ГАИ и страховые компании.  
После сбора и проработки требований и пожеланий работников автопарка, а также с учетом имеющихся технических возможностей мною был предложен и реализован следующий вариант:
- ведение списков лиц (владельцы ТС, арендаторы, покупатели, доверители и т.д.) и автомобилей в [файле Excel][1];
- подтягивание с помощью функции ВПР необходимой информации для оформления документа на специальном листе Excel при указании id-номера лиц и ТС;
- подготовка и применение для оформления документов [шаблонов Word][2] с прописанными переменными;
- считывание скриптом из [файла Excel][3] переменных и их значений с последующим заполнением шаблона документа Word.

В результате применение скрипта позволило:
- 1 раз внести данные лица или ТС в таблицу и многократно их использовать в последующем;
- хранить данные лиц и ТС в одном файле с возможностью быстрого поиска и сортировки по ним;
- автоматически формировать и добавлять в итоговый документ [словесный эквивалент][4] всех сумм (стоимость ТС при продаже, стоимость аренды, оценочная стоимость ТС);
- **в разы** сократить время и повысить качество подготовки документов с автоматическим сохранением их в отдельные папки по видам документов;
- исключить прерывание производственного процесса и временных затрат на переобучение работников автопарка, так как основная работа продолжилась в Excel и Word, а интерфейс скрипта максимально прост и понятен.

В размещенном здесь [файле][1] все данные лиц и ТС вымышлены, а в шаблонах документов реальный текст заменен на [Lorem Ipsum][5].

[1]: https://github.com/Andrei-Gu/auto_contract/blob/main/persons_and_autos.xlsx
[2]: https://github.com/Andrei-Gu/auto_contract/tree/main/templates
[3]: https://github.com/Andrei-Gu/auto_contract/blob/main/print_contract.xlsx
[4]: https://github.com/Andrei-Gu/auto_contract/tree/main/ammount_to_words
[5]: https://ru.lipsum.com/