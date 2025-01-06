inquiry_template = """
<html>
    <head>
      <title>Patient Details</title>
    </head>
    <body>
      <p>Hi,<br>
      You have received a new inquiry!
      </p>
      <table border='1'>
        <tr>
          <td><strong>Patient Name</strong></td>
          <td><strong>Patient Data</strong></td>
        </tr>
        <tr>
          <td>Patient ID</td>
          <td>{enq_id}</td>
        </tr>
        <tr>
          <td>Name</td>
          <td>{name}</td>
        </tr>
        <tr>
          <td>Location</td>
          <td>{location}</td>
        </tr>
        <tr>
          <td>Age Bracket</td>
          <td>{age}</td>
        </tr>
        <tr>
          <td>Email Address</td>
          <td>{email}</td>
        </tr>
        <tr>
          <td>Telephone Number</td>
          <td>{mobile_number}</td>
        </tr>
        <tr>
          <td>Gender</td>
          <td>{gender}</td>
        </tr>
        <tr>
          <td>Are you the patient or are you related to the patient?</td>
          <td>{relation}</td>
        </tr>
        <tr>
          <td>Is the cancer diagnosed or suspected?</td>
          <td>{diagnosis}</td>
        </tr>
        
        <tr>
          <td>Specify location of cancer</td>
          <td>{specify_location_of_cancer}</td>
        </tr>
        <tr>
          <td>Have you done any testing?</td>
          <td>{testing}</td>
        </tr>
        <tr>
        <td>Have you done any testing?</td>
        <td>{tests}</td>
      </tr>
      <tr>
        <td>Do you have medical insurance?</td>
        <td>{insurance}</td>
      </tr>
        <tr>
          <td>Have you gotten an expert second opinion?</td>
          <td>{opinion}</td>
        </tr>
        <tr>
          <td>Have you gotten an expert second opinion->Why not?</td>
          <td>{noOpinionReason}</td>
        </tr>
        <tr>
          <td>Are you interested in getting another expert opinion?</td>
          <td>{interested}</td>
        </tr>
        <tr>
        <td>Are you interested in us getting in touch with you for a detailed discussion?</td>
        <td>{discussion}</td>
      </tr>
      <tr>
        <td>Special Remark</td>
        <td>{remark}</td>
      </tr>
      </table>
    </body>
    </html>
"""

subscribe_template = """
<html>
        <head>
          <title>drbot.health</title>
        </head>
        <body>
          <p>Hi,<br>
          You have received a new subscriber!
          </p>
          <table border='1'>
            <tr>
              <td>Email Address</td>
              <td>{email}</td>
            </tr>
            <tr>
              <td>Form Type</td>
              <td>Subscribe Form</td>
            </tr>
          </table>
        </body>
        </html>
"""

contact_template = """
<html>
<head>
  <title>drbot.health</title>
</head>
<body>
  <p>Hi,<br>
  You have received a new message!
  </p>
  <table border='1'>
    <tr>
      <td>Email Address</td>
      <td>{email}</td>
    </tr>
    <tr>
      <td>Message</td>
      <td>{message}</td>
    </tr>
    <tr>
    <td>Form Type</td>
    <td>Message Form</td>
  </tr>
  </table>
</body>
</html>
"""