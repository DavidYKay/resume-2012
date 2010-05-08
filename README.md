# Resume

This started as just a simple place to store a markdown format of my resume,
and now it's turned into an easy way to host your resume using sinatra and
Heroku.

# Authors

* Nathaniel "Nat" Welch (icco)
* Dan Mayer (danmayer)

## Installation

 1. Fork this project
 2. Install the gems sinatra ( >= 1.0), rdiscount, erubis, and less
 3. To deploy to Heroku, also install the heroku gem
   * Run "heroku create"
 4. type "rake" or ./main.rb to run locally. 
 5. Edit views/style.less to make your resume look pretty.
 6. "rake deploy" to push your resume to the internet.

## TODOs

* Make tests generic from resume
* Make the resume file not included in the git repo
* gem binary and assocatiated commands (http://groups.google.com/group/rails-business/msg/68cf8a890c0d4fc8?pli=1)
* fork me on github corner banner, can be displayed on html, but not rendered to other formats
* automatic conversion to various formats HTML, LaTeX, PDF, and allow downloading in any of the formats
  * http://github.com/rtomayko/rdiscount (current)
  * http://kramdown.rubyforge.org/
  * http://maruku.rubyforge.org/ (pdf support)
  * http://github.com/alphabetum/pandoc-ruby (many formats RTF docbook man ODF slides etc)
    * http://railsforum.com/viewtopic.php?id=35844
  * http://rtomayko.github.com/ronn/ (markdown to man page)
* simpler automated deploy to heroku (possibly with staging server)
* possibly merge with a resume generator which after filling out some info via forms or yaml can generate varios resumes in all formats
  * Users could submit templates / stylesheets allowing for differently formatted resumes
* standardize gem paths lib/resume/etc
* rake task that generates proper single use gemfile and executable
* make sinatra app depend on the gem
* move the configurable files to some more explainitory path than root. 
* better filenames for the downloaded resume in various formats (currently saves as latex and markdown)
* update readme to reflect changes, updates, and new goals of the project
* change render options to disable formats if not a sinatra version of the page, render static as an option perhaps
  * or you could have the resume root which is used for opening the site via the gem be used as the root url for all the formats

## License

resume.md is property of Nathaniel "Nat" Welch. You are welcome to use it as a
base structure for your resume, but don't forget, you are not him.

The rest of the code is licensed CC-GPL. Remember sharing is caring.
