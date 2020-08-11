import pyautogui
from PIL import ImageGrab
import time

#url= https://binomo.com/

def touch_down(dat, t_cord):
    for i_ in range(1117, 1138):
        for j_ in range(300, t_cord):
            if dat[i_, j_] > 200:
                return True


def touch_up(dat, b_cord):
    for _i in range(1115, 1136):
        for _j in range(b_cord, 700):
            if dat[_i, _j] > 200:
                return True


def take_screenshot():
    img = ImageGrab.grab().convert('L')
    return img


if __name__ == '__main__':
    width, height = pyautogui.size()
    if width == 1366 and height == 768:
        T_cordinates = { 
            '80' : 383, '79' : 387, '78' : 391, '77' : 395, '76' : 399, '75' : 403, '74' : 407, '73' : 411, '72' : 415, '71' : 419, 
            '70' : 423, '69' : 427, '68' : 431, '67' : 435, '66' : 439, '65' : 443, '64' : 447, '63' : 451, '62' : 455, '61' : 459, 
            '60' : 463, '59' : 467, '58' : 471, '57' : 475, '56' : 479, '55' : 483, '54' : 487, '53' : 491, '52' : 495, '51' : 499, 
            '50' : 503, '49' : 507, '48' : 511, '47' : 515, '46' : 519, '45' : 523, '44' : 527, '43' : 531, '42' : 535, '41' : 539, 
            '40' : 543, '39' : 547, '38' : 551, '37' : 555, '36' : 559, '35' : 563, '34' : 567, '33' : 571, '32' : 575, '31' : 579, 
            '30' : 583, '29' : 587, '28' : 591, '27' : 595, '26' : 599, '25' : 603, '24' : 607, '23' : 611, '22' : 615, '21' : 619, 
            '20' : 623,
            }

        B_coordinates = {                                                                                                                                                                                        
            '20' : 624, '21' : 620, '22' : 616, '23' : 612, '24' : 608, '25' : 604, '26' : 600, '27' : 596, '28' : 592, '29' : 588, 
            '30' : 584, '31' : 580, '32' : 576, '33' : 572, '34' : 568, '35' : 564, '36' : 560, '37' : 556, '38' : 552, '39' : 548, 
            '40' : 544, '41' : 540, '42' : 536, '43' : 532, '44' : 528, '45' : 524, '46' : 520, '47' : 516, '48' : 512, '49' : 508, 
            '50' : 504, '51' : 500, '52' : 496, '53' : 492, '54' : 488, '55' : 484, '56' : 480, '57' : 476, '58' : 472, '59' : 468, 
            '60' : 464, '61' : 460, '62' : 456, '63' : 452, '64' : 448, '65' : 444, '66' : 440, '67' : 436, '68' : 432, '69' : 428, 
            '70' : 424, '71' : 420, '72' : 416, '73' : 412, '74' : 408, '75' : 404, '76' : 400, '77' : 396, '78' : 392, '79' : 388, 
            '80' : 384,
         } 

        top = input('Enter Overbought value:')
        bottom = input('Enter Oversold value:')
        t = int(input('Enter time to wait after click(in seconds):'))

        obj = take_screenshot()
        image = obj
        data = image.load()
        while(True):
            image = take_screenshot()
            data = image.load()

            if touch_down(data, T_cordinates[top]):
                pyautogui.click(x=1269, y=530)
                print('DOWN')
                time.sleep(t)

            elif touch_up(data, B_coordinates[bottom]):
                pyautogui.click(x=1278, y=463)
                print('UP')
                time.sleep(t)
