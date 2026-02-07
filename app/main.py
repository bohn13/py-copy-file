def copy_file(command: str) -> None:
    temp = command.split()

    if len(temp) != 3:
        return

    cp, src, trg = temp

    if cp != "cp":
        return

    try:
        with (open(src, "r", encoding="utf-8") as file,
              open(trg, "w", encoding="utf-8") as out):
            out.write(file.read())
    except FileNotFoundError:
        return
