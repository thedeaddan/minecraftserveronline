# minecraftserveronline
## A bot for checking online on the minecraft server
____
Need Python 3 and 4 packages:  
`python3 pip install mcstats`  
For use VK API:  
`python3 pip install vk_api`  
To output errors:  
`python3 pip install traceback`  
If package **time** is not defined:  
`python3 pip install time`
____
In order to monitor the ping and run the bot in the background, you need a **screen**:  
`sudo apt install screen`  
Start command:  
`screen -d -m -S onlinecheck python3 /projects/checkmineonline.py`  
To launch:
`screen -r onlinecheck (or just onl and he find ur procces)`  
There are 2 modes. Debug and Print:  
1. Displays information and errors.  
2. Outputs only errors.  
For Debug Mode edit line 11:  
`debug_mode = False` --> `debug_mode = True`  
For Print Mode edit line 12:  
`print_mode = False` --> `print_mode = True`  
____
![image](https://user-images.githubusercontent.com/40400854/127699039-5519bb87-18fa-4794-a375-cf18b0134c35.png)

