# cyhy-mailer #

[![Build Status](https://travis-ci.org/elr64/cyhy-mailer.svg?branch=develop)](https://travis.com/github/elr64/cyhy-mailer.svg?branch=develop)
[![Coverage Status](https://coveralls.io/repos/github/elr64/cyhy-mailer/badge.svg?branch=develop)](https://coveralls.io/github/elr64/cyhy-mailer?branch=develop)

`cyhy-mailer` is a tool for emailing Cyber Hygiene, `https-scan`, and
`trustymail` reports to the appropriate technical or distribution
e-mail addresses.

## Installation ##

After using `git` to clone the repository, you can install
`cyhy-mailer` using `pip`:

```bash
pip install /path/to/cyhy-mailer
```

Or, if you prefer, you can install directly from
[the GitHub repository](https://github.com/cisagov/cyhy-mailer):

```bash
pip install git+https://github.com/cisagov/cyhy-mailer.git
```

## Usage ##

```bash
Usage:
  cyhy-mailer report [--cyhy-report-dir=DIRECTORY]
[--tmail-report-dir=DIRECTORY] [--https-report-dir=DIRECTORY]
[--cybex-scorecard-dir=DIRECTORY] [--cyhy-notification-dir=DIRECTORY]
[--db-creds-file=FILENAME] [--batch-size=SIZE] [--summary-to=EMAILS] [--debug]
  cyhy-mailer adhoc --subject=SUBJECT --html-body=FILENAME --text-body=FILENAME
[--to=EMAILS] [--cyhy] [--cyhy-federal] [--db-creds-file=FILENAME]
[--batch-size=SIZE] [--summary-to=EMAILS] [--debug]
  cyhy-mailer (-h | --help)

Options:
  -h --help                         Show this message.
  --cyhy-report-dir=DIRECTORY       The directory where the Cyber Hygiene
                                    PDF reports are located.  If not
                                    specified then no Cyber Hygiene reports
                                    will be sent.
  --tmail-report-dir=DIRECTORY      The directory where the trustymail PDF
                                    reports are located.  If not specified then
                                    no trustymail reports will be sent.
  --https-report-dir=DIRECTORY      The directory where the https-scan PDF
                                    reports are located.  If not specified then
                                    no https-scan reports will be sent.
  --cybex-scorecard-dir=DIRECTORY   The directory where the Cybex PDF
                                    scorecard is located.  If not specified
                                    then no Cybex scorecard will be sent.
  --cyhy-notification-dir=DIRECTORY The directory where the Cyber Hygiene
                                    Notification PDF reports are located.  If
                                    not specified then no Cyber Hygiene
                                    notifications will be sent.
  -c --db-creds-file=FILENAME       A YAML file containing the Cyber
                                    Hygiene database credentials.
                                    [default: /run/secrets/database_creds.yml]
  --batch-size=SIZE                 The batch size to use when retrieving
                                    results from the Mongo database.  If not
                                    present then the default Mongo batch size
                                    will be used.
  --summary-to=EMAILS               A comma-separated list of email addresses
                                    to which the summary statistics should be
                                    sent at the end of the run.  If not
                                    specified then no summary will be sent.
  -d --debug                        A Boolean value indicating whether the
                                    output should include debugging messages
                                    or not.
  --subject=SUBJECT                 The subject line when sending an ad hoc
                                    email message.
  --html-body=FILENAME              The file containing the HTML body text
                                    when sending an ad hoc email message.
  --text-body=FILENAME              The file containing the text body text
                                    when sending an ad hoc email message.
  --to=EMAILS                       A comma-separated list of additional
                                    email addresses to which the ad hoc
                                    message should be sent.
  --cyhy                            If present, then the ad hoc message
                                    will be sent to all Cyber Hygiene
                                    agencies.
  --cyhy-federal                    If present, then the ad hoc message
                                    will be sent to all Federal Cyber
                                    Hygiene agencys.  (Note that --cyhy
                                    implies --cyhy-federal.)
```

## License ##

This project is in the worldwide [public domain](LICENSE.md).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
