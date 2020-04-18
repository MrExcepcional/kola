import time

from kola import KolaRobot
from textblob import TextBlob

def init():
    k = KolaRobot()
    # k._load_envs()
    k.open_nav()
    k.sign_in()
    k.navigate_to_job_search()
    # k.fill_job_search_box()
    # k.fill_job_location_box()
    return k

def get_jobs(robot):
    robot.get_job_search_panel()
    for _ in range(6):
        time.sleep(0.3)
        robot.scroll_down_job_search_panel()
    return robot.get_jobs_list()

def auto_search(jobs, robot):
    from trans import Translator
    trans = Translator()
    trans.open_state()
    index = 0
    num_jobs = len(jobs)
    while(index < num_jobs):
        robot.close_buena_suerte()
        jobs[index].click()
        if robot._is_applied():
            index +=1
        elif robot._is_there_apply_button():
            idioma = trans.detect(k.job_text())
            if trans.in_interest(idioma):
                input('Press enter to continue')
            elif not trans.in_avoid():
                trans.ask_classify(idioma)
            index +=1
    trans.save_state()