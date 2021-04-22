"""This module contains the PandEMessage class."""

import pystache

from cyhy.mailer.Message import Message
from cyhy.mailer.ReportMessage import ReportMessage


class PandEMessage(ReportMessage):
    """An email message with the Posture and Exposure Report attachment.

    Static attributes
    -----------------
    Subject : str
        The mustache template to use when constructing the message
        subject.

    TextBody : str
        The mustache template to use when constructing the plain text
        message body.

    HtmlBody : str
        The mustache template to use when constructing the HTML
        message body.

    """

    Subject = "Posture and Exposure Report - {{report_date}}"

    TextBody = """Greetings,

The attached Posture and Exposure (P&E) report is the result of a CISA Cyber Assessments service that provides actionable information about public exposures and security posture weaknesses.

All of the findings and information are derived from public information that is currently available. No scanning has occurred for this service.

The report will initially be delivered twice per month, but it will be updated and enhanced to integrate more data sources and be sent with greater frequency in the future. The P&E report is for your situational awareness as a supplement to other threat reports you may have internally or externally. No action is required, but your feedback and questions are more than welcome.

Note: The report is encrypted with your Cyber Hygiene password.

Thank you,
CISA Cyber Assessments - Posture and Exposure
Cybersecurity and Infrastructure Security Agency
vulnerability@cisa.dhs.gov

WARNING: This document is FOR OFFICIAL USE ONLY (FOUO). It contains information that may be exempt from public release under the Freedom of Information Act (5 U.S.G. 552). It is to be controlled, stored, handled, transmitted, distributed, and disposed of in accordance with CISA policy relating to FOUO information and is not to be released to the public or other personnel who do not have a valid 'need-to-know' without prior approval of an authorized CISA official.
"""

    HtmlBody = """<html>
<head></head>
<body>
<p>Greetings,</p>

<p>The attached Posture and Exposure (P&E) report is the result of a
CISA Cyber Assessments service that provides actionable information
about public exposures and security posture weaknesses.</p>

<p>All of the findings and information are derived from public
information that is currently available. No scanning has occurred
for this service.</p>

<p>The report will initially be delivered twice per month, but it
will be updated and enhanced to integrate more data sources and be
sent with greater frequency in the future. The P&E report is for your
situational awareness as a supplement to other threat reports you may
have internally or externally. No action is required, but your feedback
and questions are more than welcome.</p>

<p>Note: The report is encrypted with your Cyber Hygiene password.</p>

<p>Thank you,<br>
CISA Cyber Assessments - Posture and Exposure<br>
Cybersecurity and Infrastructure Security Agency<br>
<a href="mailto:vulnerability@cisa.dhs.gov">vulnerability@cisa.dhs.gov</a></p>

<p>WARNING: This document is FOR OFFICIAL USE ONLY (FOUO). It contains information that may be exempt from public release under the Freedom of Information Act (5 U.S.G. 552). It is to be controlled, stored, handled, transmitted, distributed, and disposed of in accordance with CISA policy relating to FOUO information and is not to be released to the public or other personnel who do not have a valid 'need-to-know' without prior approval of an authorized CISA official.</p>
</body>
</html>
"""

    def __init__(
        self,
        pdf_filename,
        report_date,
        to_addrs,
        from_addr=Message.DefaultFrom,
        cc_addrs=Message.DefaultCc,
        bcc_addrs=Message.DefaultBcc,
    ):
        """Construct an instance.

        Parameters
        ----------
        pdf_filename : str
            The filename of the PDF file that is the Posture and
            Exposure report corresponding to this message.

        report_date : str
            The date corresponding to the Posture and Exposure
            report attachment. We have been using dates of the
            form December 12, 2017.

        to_addrs : array of str
            An array of string objects, each of which is an email
            address to which this message should be sent.

        from_addr : str
            The email address from which this message is to be sent.

        cc_addrs : array of str
            An array of string objects, each of which is a CC email
            address to which this message should be sent.

        bcc_addrs : array of str
            An array of string objects, each of which is a BCC email
            address to which this message should be sent.

        """
        # This is the data mustache will use to render the templates
        mustache_data = {"report_date": report_date}

        # Render the templates
        subject = pystache.render(PandEMessage.Subject, mustache_data)
        text_body = pystache.render(PandEMessage.TextBody, mustache_data)
        html_body = pystache.render(PandEMessage.HtmlBody, mustache_data)

        ReportMessage.__init__(
            self,
            to_addrs,
            subject,
            text_body,
            html_body,
            pdf_filename,
            from_addr,
            cc_addrs,
            bcc_addrs,
        )
