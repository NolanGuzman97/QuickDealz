from flask import abort
from bson import ObjectId
from passlib.hash import sha256_crypt
from QuickDealzBackend.users.models import user
from QuickDealzBackend.utils.db_utils import Base
from QuickDealzBackend.utils.mail_utils import send_mail
from QuickDealzBackend.utils.helper import custom_marshal
from QuickDealzBackend.common.constants import COLLECTIONS, ACTIVATION_MAIL

base_obj = Base()

class UserService(object):
    """
    signup function
    :return:
    """
    def signup(self, payload):
        if payload.get('password') != payload.get('confirm_password'):
            abort(400, "Password does not match")
        count, records = base_obj.get(COLLECTIONS['USERS'], {"email": payload['email']})
        if count>0:
            abort(400, "Email ID Already Exists")
        payload = custom_marshal(payload, user, 'create')
        payload['password'] = sha256_crypt.encrypt(payload['password'])
        _id = base_obj.insert(COLLECTIONS['USERS'], payload)
        print(_id, type(_id))
        link = ACTIVATION_MAIL.format(id=_id)
        print(link)
        send_mail([payload['email']], "QuickDealz App Account Activation", link,
                  'signup.html', {'link': link, 'name': payload['first_name']})

    def activate(self, id):
        """
        Activate the user
        :param id:
        :return:
        """
        count, records = base_obj.get(COLLECTIONS['USERS'], {"_id":ObjectId(id)})
        if count == 0:
            abort(400, "Invalid Link")
        if records[0]['is_active']:
            abort(400, "Account Already Active")
        else:
            base_obj.update(COLLECTIONS['USERS'], {"_id": ObjectId(id)},
                            {"$set": {"is_active": True}})
