#!/usr/bin/python3
"Create a QR code business card."

import qrcode
import vobject

## CONSTANTS

F_NAME = "UPDATE"  # <-- Your fist name
L_NAME = "UPDATE"  # <-- Your last name
EMAIL = "UPDATE"  # <-- Your email address
MOBILE = "UPDATE"  # <-- Your mobile number
FILENAME = "businesscard.png"

## Create vCard

vcard = vobject.vCard()
vcard.add("n")
vcard.n.value = vobject.vcard.Name(family=L_NAME, given=F_NAME)
vcard.add("fn")
vcard.fn.value = f"{F_NAME} {L_NAME}"
vcard.add("email")
vcard.email.value = EMAIL
vcard.add("tel")
vcard.tel.value = MOBILE

## Create QR Code image

image = qrcode.make(vcard.serialize())
image.save(FILENAME)
