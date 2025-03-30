[![CI/CD GitHub Actions](https://github.com/VelikayaMish/TestPO/actions/workflows/python-test.yml/badge.svg)](https://github.com/VelikayaMish/TestPO/actions/workflows/python-test.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=VelikayaMish_TestPO&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=VelikayaMish_TestPO)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=VelikayaMish_TestPO&metric=bugs)](https://sonarcloud.io/summary/new_code?id=VelikayaMish_TestPO)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=VelikayaMish_TestPO&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=VelikayaMish_TestPO)

### План функционального тестирования
1. Идентификатор плана тестирования (ID)

      ID = Test_PO_01. 
3. Список функций для тестирования

      Тестированию подвергается одна функция вычисления корней квадратного уравнения
      function(a, b, c)
4. Подход

      Тестирование должно проходить в автоматическом режиме. В корневом каталоге проекта подготовлен файл function_test.py.
      Все тесты входят в один набор formulaTest:
      - тест test_standard_cases ожидает два корня уравнения при положительном дискриминанте; один корень уравнения при нулевом дискриминанте;
      - тест  test_complex_roots ожидает два комплексных корня уравнения при положительном комплексном дискриминанте;
      - тест test_zero_coefficient_a осуществляет проверку является ли уравнение квадратным;
      - тест test_negative_discriminant ожидает нули в обоих корнях при отрицательном дискриминанте.
5. Критерии прохождения и провала

      Тестирование проводится сравнительным утверждением assertEqual(expected, actual);, результатом которого может быть критический отказ (fatal failure). В тестируемую функцию передаются входные параметры, а результаты ее работы сравниваются с ожидаемой величиной.
      Критерием прохождения теста является точное совпадение реальной и ожидаемой величин. 
      - Положительным прохожденим теста является запись 100% tests passed, 0 tests failed out of 1. 
      - В случае отрицательного результата запись будет иметь следующий вид Error: Process completed with exit code XX., также появятся записи вида [  FAILED  ], указывающие какой конкретно тест провален.
6. Результаты тестирования

      Все тесты должны проходить успешно.
7. Инструменты и ресурсы

      Основным инструментом проверки являются библиотеки`unittest`, pytest на платформе непрерывной интеграции и непрерывной доставки CI/CD GitHub Actions.
