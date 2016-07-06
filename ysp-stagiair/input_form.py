name = raw_input("\nEnter new employee's name: ")

user_email = raw_input("\nEnter new employee's email: ")

#save Backoffice details
print "\nBACKOFFICE"
backoffice_username = raw_input("Enter Backoffice Username: ")
backoffice_pw = raw_input("Enter Backoffice pw: ")

#save Diskstation details
print "\nDISKSTATION"
diskstation_username = raw_input("Enter Diskstation Username: ")
diskstation_pw = raw_input("Enter Diskstation pw: ")

#save Wiki details
print "\nWIKI"
wiki_username = raw_input("Enter Wiki Username: ")
wiki_password = raw_input("Enter Wiki pw: ")

#greet
def be_useful():
    print "-" * len("Enter Wiki pw:" + wiki_password)
    print "Beste %s," % name
    print "\nHier zijn de login-gegevens voor de systemen die wij gebruiken:"
#backoffice creds
    print "\nBackoffice:"
    print "http://backoffice.yoursurprise.nl"
    print "username: %s" % backoffice_username
    print "ww: %s" % backoffice_pw
#diskstation creds
    print "\nDiskstation:"
    print "username: %s" % diskstation_username
    print "ww: %s" % diskstation_pw
#wiki creds
    print "\nWiki: "
    print "http://wiki.yoursurprise.nl"
    print "username: %s" % wiki_username
    print "ww: %s" % wiki_password

    print "\nHipchat:"
    print "Hipchat is een chatprogramma dat wij gebruiken voor interne communicatie."
    print "Klik op de link om een account aan te maken, gebruik hiervoor je YSP-mailadres(%s)." % user_email
    print "https://yoursurprise.hipchat.com/invite/152438/5182726a61c49f7f935d3d3a2bb9480a"

    print "\nVeel plezier bij YourSurprise!"
    print ""

be_useful()
