def textfile_read(path, encoding = "utf-8"):
    """
    Načtení textového souboru

    :param path: Cesta k souboru (string)
    :param encoding: Kódování (string)
    :return: data v podobě string (string)
    """
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as e:
        print("Chyba načtení: Soubor nebyl nalezen.")
        return False
    except Exception as e:
        print(f"{type(e)}: {e}")
    finally:
        print("todle se proved evzdy")
    return data

def textfile_write(path, txt):
    """
    Načtení textového souboru

    :param path: Cesta k souboru (string)
    :param encoding: Kódování (string)
    :return: data v podobě string (string)
    """
    result = False
    try:
        with open(path, mode="w") as file:
            file.write(txt)
            result = True
    except FileNotFoundError as e:
        print("Chyba načtení: Soubor nebyl nalezen.")
    except Exception as e:
        print(f"{type(e)}: {e}")
    finally:
        print("todle se proved evzdy")
    return result

def textfile_write_copy(src_path, dest_path, encoding = "utf-8"):
    src = textfile_read(src_path, encoding=encoding)
    with open(dest_path, encoding=encoding) as dest:
        dest.write(src)