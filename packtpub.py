import http.client, re

conn = http.client.HTTPSConnection('www.packtpub.com', 443)
login_template = 'email=%(email)s&password=%(password)s&op=Login&' \
                +'form_build_id=%(form_build_id)s&form_id=packt_user_login_form'
#Need the form_build_id, changes every page load
conn.request('GET', '/')
home = conn.getresponse().read()
re_formId = re.compile(rb'form_build_id" id="([^"]+)"')
login_values = {
    'email'         : 'user%40gmail.com',
    'password'      : 'password123',
    'form_build_id' : re.search(re_formId, home).group(1)
  }
#TODO add headers and cookies


conn.request('POST', '/packt/offers/free-learning', login_template %login_values)
r = conn.getresponse()
print(r.read())
