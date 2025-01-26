# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import zipfile
    import pandas as pd
    import os

    def extract_files(zip_path, extract_to):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

    def get_txt_files(directory):
        txt_files = []
        for root, _, files_in_dir in os.walk(directory):
            txt_files.extend([os.path.join(root, file) for file in files_in_dir if file.endswith(".txt")])
        return txt_files

    def read_files_to_dict(files):
        data = {"test": {"phrase":[], "target":[]}, "train": {"phrase":[], "target":[]}}
        for file_path in files:
            with open(file_path, "r") as file:
                phrase = file.read()
            target = file_path.split(os.sep)[-2]
            data_type = "test" if "test" in file_path else "train"
            data[data_type]["phrase"].append(phrase)
            data[data_type]["target"].append(target)
        return data

    def save_dataframes(data, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for key, value in data.items():
            df = pd.DataFrame(value)
            df.to_csv(os.path.join(output_dir, f"{key}_dataset.csv"), index=False)


    zip_path = "files/input.zip"
    extract_to = "files"
    input_dir = os.path.join(extract_to, "input")
    output_dir = os.path.join(extract_to, "output")

    extract_files(zip_path, extract_to)
    txt_files = get_txt_files(input_dir)
    data = read_files_to_dict(txt_files)
    save_dataframes(data, output_dir)



pregunta_01()