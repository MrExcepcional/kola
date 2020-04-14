from kola import KolaRobot

k = KolaRobot()
k._load_envs()
k.open_nav()
k.sign_in()
k.navigate_to_job_search()