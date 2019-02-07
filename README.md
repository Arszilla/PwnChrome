# PwnChrome
A small program that grabs saved passwords from Chrome using a vulnerability where saved passwords are vulnerable to attacks/grabs when Chrome is closed.

Based on/Inspired from [w3w3w3 - ncorbuk](https://github.com/ncorbuk)'s [code](https://github.com/ncorbuk/Google-Chrome-Browser-Database-Hack).

## Requirements
- Python 3.3+
- [pywin32 module](https://github.com/mhammond/pywin32) - The program will automatically install this module if you don't have it

## Information
To run the script just launch the `PwnChrome.py` using `python PwnChrome.py`.

The script will automatically detect the operating system (Windows/MacOS/Linux) and if the operating system is Windows, it will navigate to Chrome's saved passwords directory accordingly. From there on it will access the saved passwords; which are unprotected while Chrome is closed and extract the `url`, `username` and `password` to `PwnChrome.txt` which will be placed where the `PwnChrome.py` is at. 

The script will automatically detect if your operating system is supported, check if `pywin32` is installed and if it isn't it will install it for you. From there on it will check if `chrome.exe` is running and if it is running it will kill the task so it can grab the data and paste it in `PwnChrome.txt` which will be placed where your `PwnChrome.py` is at.

For now Windows is the only operating system that this script works on. This is due to `pywin32` not working on MacOS or Linux mainly due to the fact that `pywin32` provides access to many of the Windows' APIs from Python; meaning it requires Windows. I am looking for ways to decrypt  OS X Keychain for MacOS and GNOME Keyring or KWallet on Linux. 

This project is for educational purposes **ONLY**.

Written with Python 3.7.

## Acknowledgements
- [w3w3w3 - ncorbuk](https://github.com/ncorbuk) for the [original code](https://github.com/ncorbuk/Google-Chrome-Browser-Database-Hack).

## Disclaimer
This project is for educational purposes **ONLY**. As the MIT License states:

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._

## Donations
If you'd like to donate to me use one of these two methods please:

**Bitcoin Cash:** [bitcoincash:qppxw4t8zqm4cp8gpvaldx4sur2f4e8wvgqecnl4ld](https://i.imgur.com/rwIhn3b.png)

**Bitcoin:** [1FBGXoAMSEmZwnbzyjQ81eo72EGU8hjV7A](https://i.imgur.com/6wxQ9G0.png)
