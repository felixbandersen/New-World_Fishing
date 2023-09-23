from robocorp.tasks import task
from RPA.Desktop import Desktop
from random import randrange
import random
import time

d = Desktop()









@task
def minimal_task():
    #Making an forever loop.
    loop = True
    while loop == True:
        #------------------AFK PREVENTION------------------
        #Preventing being kicked out of the game.
        afk_prevention()
        
        #---------------------BROKEN?----------------------
        #Checks if fishing pole is broken.
        broken=cast_ui()
        print(f'Is fishingpole broken? {broken}')
        if broken == True:
            broken_fishing_pole()
            continue

        #----------------------CAST------------------------
        #Sets cast time and casts the "bait".
        cast_time = random.uniform(1, 2)
        print(f'It took: {cast_time}seconds to cast.')
        cast(cast_time)
        #If the cast fails it will restart the loop.
        try:
            cast_into_water()
        except:
            time.sleep(7)
            continue
        
        #----------------------REEL 'EM INN-----------------
        #Reeling in the "bait".
        reel_it_inn()



def afk_prevention():
    print('Moving back and forward for afk prevention')
    d.press_keys("s")
    d.press_keys("w")

def cast_ui():
    try:
        f3_visible=d.find_element('image:data/f3.png')
        print('We are still fishing!')
    except:
        print('Fishing interface is missing, Trying to repair pole..')
        broken_fishing_pole = True
        return broken_fishing_pole

def broken_fishing_pole():
    try:
        d.press_keys('f3')
        d.wait_for_element('image:data/broken_fishingpole.png', timeout=5, interval=0.2)
        print('Fishing pole is broken!!')
        d.press_keys('tab')
        d.click('image:data/repair.png')
        d.click('image:data/confirm_repair.png')
        d.press_keys('tab')
        time.sleep(3)
        d.press_keys('f3')
        time.sleep(2)
        broken = True
        return broken
    except:
        print('Fishing pole is not broken! We keep on fishing!')
        return False


def cast(cast_time: int):
    d.press_mouse_button()
    time.sleep(cast_time)
    d.release_mouse_button()


def cast_into_water():
    hook=d.wait_for_element('image:data/hook.png', timeout=120, interval=0.2)
    d.click(hook)
    

def reel_it_inn():
    result = None
    while result is None:
        try:
            d.find_element('image:data/f3.png')
            result = True
        except:
            reel_time = random.uniform(1, 2.5)
            reel_sleep = random.uniform(0.75, 1.5)
            print(f'Reeling in the fish! {reel_time}second hold!')
            d.press_mouse_button()
            time.sleep(reel_time)
            d.release_mouse_button()
            time.sleep(reel_sleep)
            







