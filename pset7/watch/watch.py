# I couldn't find any information about an oficial patter for Youtube video's identifiers
# I did that pset based on 2 assumptions:
# First, every youtube video has 11 characters long
# Second, those characters can only be alphanumerical characters, hiffen and underscore:
# https://community.latenode.com/t/regular-expression-pattern-to-validate-youtube-video-urls/20790
# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video

import re


def main():
    print (parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^<iframe(?:\w*)? src=\"(?:https?://)?(?:www.)?youtube\.com/embed/([\w-]{11})\"", s):
        return "https://youtu.be/" + matches.group(1)
    
    
if __name__ == "__main__":
    main()
