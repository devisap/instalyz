import smtplib #importing the module
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(dataset):
   sender_add='181111060@mhs.stiki.ac.id' #storing the sender's mail id
   receiver_add=dataset[0] #storing the receiver's mail id
   password='ssri2000+*27gOsT' #storing the password to log in

   #creating the SMTP server object by giving SMPT server address and port number
   smtp_server=smtplib.SMTP("smtp.gmail.com",587)
   smtp_server.ehlo() #setting the ESMTP protocol

   smtp_server.starttls() #setting up to TLS connection
   smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()

   smtp_server.login(sender_add,password) #logging into out email id

   msg = MIMEMultipart('alternative')
   msg['Subject'] = "SUCCESSFULLY"
   msg['From']    = sender_add
   msg['To']      = receiver_add
   
   msg.attach(MIMEText(template(dataset), 'html'))

   smtp_server.sendmail(sender_add,receiver_add, msg.as_string())
   print('Successfully the mail is sent')

   smtp_server.quit()

def template(dataset):
   return """
      <!DOCTYPE html>
         <html lang="en">
         <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <!-- Font -->
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

            <!-- CSS Implementing Plugins -->
            <link rel="stylesheet" href="<?= site_url()?>assets/vendor/bootstrap-icons/font/bootstrap-icons.css">

            <!-- CSS Front Template -->
            <!-- <link rel="stylesheet" href="<?= site_url()?>assets/css/theme.min.css"> -->
            <style>
               ::after,
               ::before {
                     box-sizing: border-box;
               }
               .h1,
               .h2,
               .h3,
               .h4,
               .h5,
               .h6,
               h1,
               h2,
               h3,
               h4,
               h5,
               h6 {
                     margin-top: 0;
                     margin-bottom: 0.5rem;
                     font-weight: 600;
                     line-height: 1.2;
                     color: #1e2022;
                     font-family: Inter, sans-serif;
               }
               .h4,
               h4 {
                     font-size: 1.125rem;
               }
               p{
                     font-family: Inter, sans-serif;
                     font-size: 1rem;
                     color: #677788;
                     font-weight: 400;
                     line-height: 1.5;
               }
               a {
                     color: #922C88;
                     text-decoration: none;
                     font-family: Inter, sans-serif;
               }
               a:hover {
                     color: #5c0d54;
               }
               .small,
               small {
                     font-size: 0.875em;
                     font-family: Inter, sans-serif;
                     color: #677788;
                     font-weight: 400;
                     line-height: 1.5;
               }
               .mb-0 {
                     margin-bottom: 0 !important;
               }
               .mb-1 {
                     margin-bottom: 0.25rem !important;
               }
               .mb-2 {
                     margin-bottom: 0.5rem !important;
               }
               .mb-3 {
                     margin-bottom: 1rem !important;
               }
               .mb-4 {
                     margin-bottom: 1.5rem !important;
               }
               .mb-5 {
                     margin-bottom: 2rem !important;
               }
               .mb-6 {
                     margin-bottom: 2.5rem !important;
               }
               .mb-7 {
                     margin-bottom: 3rem !important;
               }
               .mb-8 {
                     margin-bottom: 3.5rem !important;
               }
               .mb-9 {
                     margin-bottom: 4rem !important;
               }
               .mb-10 {
                     margin-bottom: 4.5rem !important;
               }
               .mb-auto {
                     margin-bottom: auto !important;
               }
               .mb-2{
                     margin-bottom: 0.5rem!important;
               }
               .card {
                     background: #fff;
                     border-width: 0;
                     box-shadow: 0 0.375rem 1.5rem 0 rgba(140, 152, 164, 0.125);
                     border-radius: 0.5rem !important;
               }
               .navbar-brand-logo {
                     width: 100%;
                     min-width: 7.5rem;
                     max-width: 7.5rem;
               }
               .card-body {
                     -ms-flex: 1 1 auto;
                     flex: 1 1 auto;
                     padding: 2rem 2rem;
               }
               .text-primary {
                     opacity: 1;
                     color: #DC06D8 !important;
               }
               .text-highlight-warning {
                     background: left 1em/1em 0.2em;
                     background-repeat: repeat-x;
                     background-image: linear-gradient(to bottom, rgba(243, 143, 4, 0.5), rgba(243, 143, 4, 0.5));
               }
               .row {
                     --bs-gutter-x: 1.5rem;
                     --bs-gutter-y: 0;
                     display: flex;
                     flex-wrap: wrap;
                     margin-top: calc(var(--bs-gutter-y) * -1);
                     margin-right: calc(var(--bs-gutter-x) * -0.5);
                     margin-left: calc(var(--bs-gutter-x) * -0.5);
               }
               .row>* {
                     flex-shrink: 0;
                     width: 100%;
                     max-width: 100%;
                     padding-right: calc(var(--bs-gutter-x) * 0.5);
                     padding-left: calc(var(--bs-gutter-x) * 0.5);
                     margin-top: var(--bs-gutter-y);
               }
               .col-1 {
               flex: 0 0 auto;
               width: 8.33333333%;
               }

               .col-2 {
               flex: 0 0 auto;
               width: 16.66666667%;
               }

               .col-3 {
               flex: 0 0 auto;
               width: 25%;
               }

               .col-4 {
               flex: 0 0 auto;
               width: 33.33333333%;
               }

               .col-5 {
               flex: 0 0 auto;
               width: 41.66666667%;
               }

               .col-6 {
               flex: 0 0 auto;
               width: 50%;
               }

               .col-7 {
               flex: 0 0 auto;
               width: 58.33333333%;
               }

               .col-8 {
               flex: 0 0 auto;
               width: 66.66666667%;
               }

               .col-9 {
               flex: 0 0 auto;
               width: 75%;
               }

               .col-10 {
               flex: 0 0 auto;
               width: 83.33333333%;
               }

               .col-11 {
               flex: 0 0 auto;
               width: 91.66666667%;
               }

               .col-12 {
               flex: 0 0 auto;
               width: 100%;
               }

               .offset-1 {
               margin-left: 8.33333333%;
               }

               .offset-2 {
               margin-left: 16.66666667%;
               }

               .offset-3 {
               margin-left: 25%;
               }

               .offset-4 {
               margin-left: 33.33333333%;
               }

               .offset-5 {
               margin-left: 41.66666667%;
               }

               .offset-6 {
               margin-left: 50%;
               }

               .offset-7 {
               margin-left: 58.33333333%;
               }

               .offset-8 {
               margin-left: 66.66666667%;
               }

               .offset-9 {
               margin-left: 75%;
               }

               .offset-10 {
               margin-left: 83.33333333%;
               }

               .offset-11 {
               margin-left: 91.66666667%;
               }
               .col-md-1 {
                     flex: 0 0 auto;
                     width: 8.33333333%;
               }

               .col-md-2 {
                     flex: 0 0 auto;
                     width: 16.66666667%;
               }
               .col-md-3 {
                     -ms-flex: 0 0 auto;
                     flex: 0 0 auto;
                     width: 25%;
               }
               .col-md-6 {
                     -ms-flex: 0 0 auto;
                     flex: 0 0 auto;
                     width: 50%;
               }
               .col-md-8 {
                     flex: 0 0 auto;
                     width: 66.66666667%;
               }
               .col-md-10 {
                     flex: 0 0 auto;
                     width: 83.33333333%;
               }

               .col-md-11 {
                     flex: 0 0 auto;
                     width: 91.66666667%;
               }

               .col-md-12 {
                     flex: 0 0 auto;
                     width: 100%;
               }
               .offset-md-0 {
                     margin-left: 0;
               }

               .offset-md-1 {
                     margin-left: 8.33333333%;
               }

               .offset-md-2 {
                     margin-left: 16.66666667%;
               }

               .offset-md-3 {
                     margin-left: 25%;
               }

               .offset-md-4 {
                     margin-left: 33.33333333%;
               }

               .offset-md-5 {
                     margin-left: 41.66666667%;
               }

               .offset-md-6 {
                     margin-left: 50%;
               }

               .offset-md-7 {
                     margin-left: 58.33333333%;
               }

               .offset-md-8 {
                     margin-left: 66.66666667%;
               }

               .offset-md-9 {
                     margin-left: 75%;
               }

               .offset-md-10 {
                     margin-left: 83.33333333%;
               }

               .offset-md-11 {
                     margin-left: 91.66666667%;
               }
               .col-sm-1 {
                     flex: 0 0 auto;
                     width: 8.33333333%;
               }

               .col-sm-2 {
                     flex: 0 0 auto;
                     width: 16.66666667%;
               }

               .col-sm-3 {
                     flex: 0 0 auto;
                     width: 25%;
               }

               .col-sm-4 {
                     flex: 0 0 auto;
                     width: 33.33333333%;
               }

               .col-sm-5 {
                     flex: 0 0 auto;
                     width: 41.66666667%;
               }

               .col-sm-6 {
                     flex: 0 0 auto;
                     width: 50%;
               }

               .col-sm-7 {
                     flex: 0 0 auto;
                     width: 58.33333333%;
               }

               .col-sm-8 {
                     flex: 0 0 auto;
                     width: 66.66666667%;
               }

               .col-sm-9 {
                     flex: 0 0 auto;
                     width: 75%;
               }

               .col-sm-10 {
                     flex: 0 0 auto;
                     width: 83.33333333%;
               }

               .col-sm-11 {
                     flex: 0 0 auto;
                     width: 91.66666667%;
               }

               .col-sm-12 {
                     flex: 0 0 auto;
                     width: 100%;
               }

               .offset-sm-0 {
                     margin-left: 0;
               }

               .offset-sm-1 {
                     margin-left: 8.33333333%;
               }

               .offset-sm-2 {
                     margin-left: 16.66666667%;
               }

               .offset-sm-3 {
                     margin-left: 25%;
               }

               .offset-sm-4 {
                     margin-left: 33.33333333%;
               }

               .offset-sm-5 {
                     margin-left: 41.66666667%;
               }

               .offset-sm-6 {
                     margin-left: 50%;
               }

               .offset-sm-7 {
                     margin-left: 58.33333333%;
               }

               .offset-sm-8 {
                     margin-left: 66.66666667%;
               }

               .offset-sm-9 {
                     margin-left: 75%;
               }

               .offset-sm-10 {
                     margin-left: 83.33333333%;
               }

               .offset-sm-11 {
                     margin-left: 91.66666667%;
               }
               .btn{
                     display: inline-block;
                     font-weight: 400;
                     line-height: 1.5;
                     color: #DC06D8;
                     text-align: center;
                     vertical-align: middle;
                     cursor: pointer;
                     -webkit-user-select: none;
                     -moz-user-select: none;
                     -ms-user-select: none;
                     user-select: none;
                     background-color: transparent;
                     border: 0.0625rem solid transparent;
                     padding: 0.6125rem 1rem;
                     font-size: 1rem;
                     border-radius: 0.3125rem;
                     transition: all 0.2s ease-in-out;
               }
               .btn-soft-primary{
                     color: #DC06D8;
                     background-color: rgba(220, 6, 216, 0.1);
                     border-color: transparent;
               }
               .btn-soft-primary:hover {
                     color: #fff;
                     background-color: #DC06D8;
               }
            </style>
         </head>
         <body style="background: #f2f2f2;padding-top: 50px;padding-bottom: 50px;padding-left: 50px;padding-right: 50px;">
            <div class="card">
               <div class="card-body">
                     <div  class="mb-4" style="text-align: center;">
                        <img src="https://istanbulyouthsummit.com/instalyze.png" style="width: 150px;"/>
                     </div>
                     <h2 class="mt-1 mb-4">Welcome to <span class="text-primary text-highlight-warning">Instalyze</span>.</h2>
                     <p class="mb-2">
                        Congratulations, the #"""+dataset[2]+""" hashtag analysis has been released. You can also see it on the instalyze web right now!
                     </p>
                     <table class="mb-4">
                        <tr>
                           <td>Total Post</td>
                           <td>: </td>
                           <td style="font-weight: bold;">"""+str(dataset[3])+"""</td style="font-weight: bold;">
                        </tr>
                        <tr>
                           <td>Total Like</td>
                           <td>: </td>
                           <td style="font-weight: bold;">"""+str(dataset[4])+"""</td style="font-weight: bold;">
                        </tr>
                        <tr>
                           <td>Total Comment</td>
                           <td>: </td>
                           <td style="font-weight: bold;">"""+str(dataset[5])+"""</td style="font-weight: bold;">
                        </tr>
                        <tr>
                           <td>Top Post</td>
                           <td>: </td>
                           <td style="font-weight: bold;"><a target="_blank" href="https://instagram.com/p/"""+dataset[6]+"""">Link</a></td style="font-weight: bold;">
                        </tr>
                        <tr>
                           <td>Top Influencer</td>
                           <td>: </td>
                           <td style="font-weight: bold;"><a target="_blank" href="https://instagram.com/"""+dataset[7]+""""">"""+dataset[7]+""""</a></td style="font-weight: bold;">
                        </tr>
                     </table>
                     <a href="127.0.0.1/instalyze-front/overview" class="btn btn-soft-primary mb-6">Go to web</a>
               </div>
            </div>
         </body>
         </html>
   """
   