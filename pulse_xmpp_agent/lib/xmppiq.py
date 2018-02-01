#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# (c) 2016 siveo, http://www.siveo.net
#
# This file is part of Pulse 2, http://www.siveo.net
#
# Pulse 2 is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Pulse 2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pulse 2; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import json
import logging

DEBUGPULSE = 25

def callXmppFunctionIq(functionname,  *args, **kwargs):
    logging.getLogger().debug("**call function %s %s %s"%(functionname, args, kwargs))
    return getattr(functionsynchroxmpp,functionname)(*args, **kwargs)

def dispach_iq_command(xmppobject, jsonin):
    """
        this function doit retirner un json string
    """
    data = json.loads(jsonin)

    listactioncommand = ["xmppbrowsing", "test", "remotefile"]
    if data['action'] in listactioncommand:
        logging.log(DEBUGPULSE,"call function %s "%data['action'] )
        result = callXmppFunctionIq(data['action'],  xmppobject = xmppobject, data = data )
        if type(result) != str:
            logging.getLogger().warning("function %s not return str json"%data['action'])
        return result
    else:
        logging.log(DEBUGPULSE,"function %s missing in list listactioncommand"%data['action'] )
        return ""


class functionsynchroxmpp:
    """
        this function must return json string 
    """
    @staticmethod
    def xmppbrowsing(xmppobject , data  ):
        return json.dumps(data)

    @staticmethod
    def test( xmppobject, data):
        return json.dumps(data)

    @staticmethod
    def remotefile( xmppobject, data ):
        datapath = data['data']
        print type(datapath)
        if type(datapath) == unicode or type(datapath) == str:
            datapath = str(data['data'])
            filesystem = xmppobject.xmppbrowsingpath.listfileindir(datapath)
            print filesystem
            data['data']=filesystem
        return json.dumps(data)