import schedule
import dwh_main

if __name__ == '__main__':
    dwh_main.main()
    schedule.every().day.at('16:09:00').do(dwh_main.main)
    while True:
        schedule.run_pending()
