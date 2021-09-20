# Lesson 2

There are eight downloadable exercises in Lesson 2 of this course.

* The hello server
* The echo server
* HTML forms
* The messageboard server, part one (POST requests)
* The messageboard server, part two (GET and POST)
* The messageboard server, part three (POST-Redirect-GET)
* The JSON client demo
* The bookmark server

## My Observations
- The messageboard handles two POST request from my Firefox browser and saves two `message` similar string each time I interract with the submit button.
    - Button clicks
    - `Tab` and `enter`
    - `Tab` and `spacebar`
- The Firefox Debugger Network tab is reporting only one sent POST request and one received GET request.
- I might troubleshoot this from tcpdump later on.(I'm kind of new to tcpdump)
- Chrome behaves as expected.


I also just noticed that changing the file permissions alerts git of a change in the tracked files or folders