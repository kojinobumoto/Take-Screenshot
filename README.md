# Take the screenshot of the specified URLs.
* Saves a full screen screenshot as a png image file.
* The browser is not visually displayed because chromedriver is running in headless mode to capture the full screen.
* Since chrome in eadless mode does not support BASIC authentication, this tool does not support BASIC authentication either.
    * "The team owning Headleass Chrome has decided not to support extensions."
    * https://bugs.chromium.org/p/chromedriver/issues/detail?id=2342
    * https://bugs.chromium.org/p/chromium/issues/detail?id=706008
# Usage and how it runs.
* Enter the target URL (and ID) in a CSV file in the following format. The file will be read and the screenshot will be acquired.
    * Format
        * ID,URL
            * Only ASCII characters can be specified for ID (no multibyte characters)
            * [Reason] Because OpenCV does not accept double-byte characters in the filename when using it in the next step (#Image Difference with OpenCV").
    * write 1 URL per line.
    * Save the file in UTF-8 encoding.
    * The file of URL lists to be placed directly under the ". /url-lists" folder.
    * Interactively select the URL lists (CSV file) name under the "./url-lists" to load.
* The program aves the screenshot as "ID.png".
    * location of ghe saved png image.
        * The 'screenshot-YYYYYYMMDD-hhmmss' directory (where YYYYYMMDD-HHMMS is the start date and time) just under the directory where this program is run.
* By default, processes are created for the number of CPU cores in the execution environment and processed in parallel. To adjust, change the "num_processors" variable.
* The results of the execution (the pair of the URL and the png image file name) are output as a CSV file named "results-YYYYYMMMDD-HHMMMSS.csv" (the YYYYYMMDD-HHMMMSS part corresponds to the directory name where the image is saved).
