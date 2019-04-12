<p align="center">
  <a href="https://github.com/Arszilla/PwnChrome/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Arszilla/PwnChrome.svg?logo=github&logoColor=white"></a>
  <a href="http://www.python.org/download/"><img alt="Python 3.3+" src="https://img.shields.io/badge/Python-3.3+-yellow.svg?color=blue&logo=python&logoColor=white"></a>
</p>

# PwnChrome
A small program that grabs saved passwords from Chrome using a vulnerability where saved passwords are vulnerable to 
attacks/grabs when Chrome is closed.

## Requirements
- Python 3.3+
- [pywin32 module](https://github.com/mhammond/pywin32) - The program will automatically install this module if you 
don't have it

## Information
To run the script just launch the `PwnChrome.py` using `python PwnChrome.py`.

The script will automatically detect the operating system (Windows/MacOS/Linux) and if the operating system is Windows, 
it will check if you have `pywin32` module and if you don't have it the script will install it for you. Afterwards the 
script will check if `chrome.exe` is running and if it is running it will kill it so it can navigate to Chrome's saved 
passwords directory and access the saved passwords; which are unprotected while Chrome is closed. From there it will 
extract the `url`, `username` and `password` to `PwnChrome.txt` which will be placed where the `PwnChrome.py` is at. 

The reason why the script checks if your operating system is Windows' is because `pywin32` cannot be installed in MacOS 
or Linux mainly due to `pywin32` requring Windows since it provides access to many of the Windows' APIs for Python. 
I am looking for ways to decrypt  OS X Keychain for MacOS and GNOME Keyring or KWallet on Linux. 

This project is for educational purposes **ONLY**.

Written with Python 3.7.

## Acknowledgements
- [w3w3w3 - ncorbuk](https://github.com/ncorbuk) for the [original code](https://github.com/ncorbuk/Google-Chrome-Browser-Database-Hack) & exploit.

## Disclaimer
This project is for educational purposes **ONLY**. As the MIT License states:

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._

## Donations
If you'd like to donate to me use one of these two methods please:

**Bitcoin Cash:** [bitcoincash:qppxw4t8zqm4cp8gpvaldx4sur2f4e8wvgqecnl4ld](https://i.imgur.com/rwIhn3b.png)

**Bitcoin:** [1FBGXoAMSEmZwnbzyjQ81eo72EGU8hjV7A](https://i.imgur.com/6wxQ9G0.png)
