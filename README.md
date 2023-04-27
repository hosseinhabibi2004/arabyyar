<p align="center">
  <a href="" rel="noopener">
  <img src="https://github.com/VoltaCore/ArabyYar/blob/master/Web/media/static/img/label.png" alt="ArabyYar"></a>
</p>

---

<p align="center">
  <b>ArabyYar</b> a browser-based app for learning Arabic simple - v1.0.1
  <br> 
</p>

---
## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Complie To Exe](#compile_to_exe)
- [Built Using](#built_using)

---
## 🏁 Getting Started <a name = "getting_started"></a>

After cloning the project install python required libraries using this command:

```bash
pip install -r requirements.txt
```

Now you can run the project by starting **app.py**

```bash
python app.py
```

---
## 🗜 Complie To Exe <a name = "compile_to_exe"></a>

For running the application on other devices with Windows operating system without installing Python and other requirements we need to compile the program to [exe](https://en.wikipedia.org/wiki/.exe).

We need [Pyinstaller](https://pypi.org/project/pyinstaller/) library for converting **py** to **exe**:

```bash
pip install pyinstaller
```
---
Working with Pyinstaller is not hard but we can make it even easier using [Auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) :

```bash
pip install auto-py-to-exe
```

After installing **auto-py-to-exe** open [cmd](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) and run **auto-py-to-exe**:

```bash
auto-py-to-exe
```
---
Replace below code in *settings.py*:
```python
import sys
Web_Template_Folder = '\\'.join((sys._MEIPASS.replace('/', '\\'), 'Web\\media\\templates', ))
Web_Static_Folder = '\\'.join((sys._MEIPASS.replace('/', '\\'), 'Web\\media\\static', ))
```

Replace Below Code instead of `app = Flask(__name__, template_folder=settings.Web_Template_Folder, static_folder=settings.Web_Static_Folder)` in *Web/\_\_init\_\_.py* :

```python
import sys
if getattr(sys, 'frozen', False):
    app = Flask(__name__, template_folder=settings.Web_Template_Folder, static_folder=settings.Web_Static_Folder)
else:
    app = Flask(__name__)
```

Use this command for start converting **py** to **exe**: (Use `--onefile` for one file exe | Use `--onedir` for exe in one directory)

```bash
pyinstaller --noconfirm --onefile --windowed --icon "<ICO File Address>" --name "Araby Yar" --add-data "<settings.py address>;." --add-data "<Desktop Directory Address>;Desktop/" --add-data "<Web Directory Addres>;Web/"  "<app.py Address>"
```

---
## ⛏️ Built Using <a name = "built_using"></a>

**[Python](https://python.org/)** - An interpreted, high-level and general-purpose programming language

> - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Micro web framework written in Python
> - [PyArabic](https://pypi.org/project/PyArabic/) - A specific Arabic language library
> - [libqutrub](https://pypi.org/project/libqutrub/) - Arabic verb conjugation software
> - [PyQt5](https://pypi.org/project/PyQt5/) - PyQt5 is a comprehensive set of Python bindings for Qt v5


**[JavaScript](https://javascript.com/)** - A programming language that conforms to the ECMAScript specification

> - [Alertify](https://alertifyjs.com/) - A framework for developing pretty browser dialogs and notifications.
> - [jQuery](https://jquery.com/) - A Library designed to simplify HTML DOM tree traversal and manipulation
> - [Bootstrap](https://getbootstrap.com/) - A free and open-source CSS framework directed at responsive, mobile-first front-end web development.

---
## ✍️ Authors <a name = "authors"></a>

- [Moein Akbari](https://github.com/Moein-Akbari)
- [Hossein Habibi](https://github.com/Hossein-Habibi-2004)
- [Ali Mohammadi](https://github.com/ali-mohamadi)
