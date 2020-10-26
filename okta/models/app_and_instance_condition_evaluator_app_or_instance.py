# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class AppAndInstanceConditionEvaluatorAppOrInstance(
    OktaObject
):
    """
    A class for AppAndInstanceConditionEvaluatorAppOrInstance objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.id = config["id"]\
                if "id" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.id = None
            self.name = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "id": self.id,
            "name": self.name,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format