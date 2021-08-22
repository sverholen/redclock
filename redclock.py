import logging
from redminelib import Redmine
from apps.work import WorkPeriod
import time
from time import strftime
from sqlalchemy import create_engine, text


logger = logging.getLogger(__name__)


def main():
    engine = create_engine("sqlite+pysqlite:///redclock.sqlite3", echo=True, future=True)

    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())

    url = "https://redmine.inuits.eu/"
    key = "432a7425c0032de9f4ed9be8ba1d540898d74e2a"
    project_name = 'scouts-kampvisum'

    redmine = Redmine(url, key=key)
    project = redmine.project.get(project_name)

    issue = redmine.issue.get(81325)

    work = WorkPeriod()
    work.issue = issue

    work.start()
    time.sleep(2)
    work.stop()

    #time_spent = '{0:%H:%M:%S}'.format(work.time_spent())
    #time_spent = strftime("%H:%M:%S", (work.time_spent(), ))
    print("Worked on issue for ", work.time_spent())

    print(issue)

if __name__ == "__main__":
    # execute only if run as a script
    main()