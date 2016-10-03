Settings

Look in settings.py for a full list of all the configuration options. Here's a high level overview:



Docker

Create a folder called config, then put a file called private.py inside.
Specify new values for any of the settings above in private.py.
For example, you could put AREAS = ['sfc'] in private.py to only look in San Francisco.
If you want to post into a Slack channel not called housing, add an entry for SLACK_CHANNEL.
If you don't want to look in the Bay Area, you'll need to update the following settings at the minimum:


Manual


Docker

Make sure to do the steps in the configuration section above first.
Install Docker by following these instructions.
To run the program with the default configuration:
docker run -d -e SLACK_TOKEN={YOUR_SLACK_TOKEN} dataquestio/apartment-finder
To run the program with your own configuration:
docker run -d -e SLACK_TOKEN={YOUR_SLACK_TOKEN} -v {ABSOLUTE_PATH_TO_YOUR_CONFIG_FOLDER}:/opt/wwc/apartment-finder/config dataquestio/apartment-finder
Manual

Look in the Dockerfile, and make sure you install any of the apt packages listed there.
Install Python 3 using Anaconda or another method.
Install the Python requirements with pip install -r requirements.txt.
Run the program with python main_loop.py. Results will be posted to your #Housing channel if successful.
Troubleshooting

Docker

Use docker ps to get the id of the container running the bot.
Run docker exec -it {YOUR_CONTAINER_ID} /bin/bash to get a command shell inside the container.
Run sqlite listings.db to run the sqlite command line tool and inspect the database state (the only table is also called listings).
select * from listings will get all of the stored listings.
If nothing is in the database, you may need to wait for a bit, or verify that your settings aren't too restrictive and aren't finding any listings.
You can see how many listings are being found by looking at the logs.
Inspect the logs using tail -f -n 1000 /opt/wwc/logs/afinder.log.

Manual

Look at the stdout of the main program.
Inspect listings.db to ensure listings are being added.

Deploying

Create a server that has Docker installed. It's suggested to use Digital Ocean.
Follow the configuration + installation instructions for Docker above.