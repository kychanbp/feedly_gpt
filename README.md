# Feedly GPT
Summarize RSS Feed in Feedly using ChatGPT

## Get RSS Feed From Feedly
* Using Official Feedly [python-api-client](https://github.com/feedly/python-api-client#readme)
    * The [python-api-client](https://github.com/feedly/python-api-client#readme) was cloned into the `python-api-client` folder, and installed using `pip`. More instructions can be found in the [python-api-client](https://github.com/feedly/python-api-client#readme)

* Originally want to use [Sandbox](https://groups.google.com/g/feedly-cloud) for development but [sandbox is downed until further notice](https://groups.google.com/g/feedly-cloud/c/5hZlpqgJLXM). So I used [Feedly Developer Token](https://developer.feedly.com/v3/developer/). The limitation is that the token has a limit of 25 API requests per day and is going to expire in 30 days.

* the [opml file](https://developers.feedly.com/v3/opml/) does not seem to contain contents.

* the original python-api-client does not provide all the options in StreamOption. I have to modify the class to include more options.