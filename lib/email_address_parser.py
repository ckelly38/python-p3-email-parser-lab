import re;

class EmailAddressParser:
    def __init__(self, eadrssstr):
        self.emailaddressstr = eadrssstr;

    def parse(self):
        regex = re.compile(r",\s|\s|,");
        mlist = list(set(re.split(regex, self.emailaddressstr)));
        retlist = [];
        email_address = r"[A-z][A-z0-9._]*@[A-z]*\.[A-z]*";
        email_regex = re.compile(email_address);
        for item in mlist:
            if (re.fullmatch(email_regex, item)): retlist.append(item);
        return sorted(retlist);
        #return list(set(self.emailaddressstr.split(", ")));

parser = EmailAddressParser("john@doe.com, person@somewhere.org, who, what, where, when, why, how");
print(parser.parse());
