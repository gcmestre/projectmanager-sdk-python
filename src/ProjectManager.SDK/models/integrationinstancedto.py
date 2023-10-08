#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class IntegrationInstanceDto:
    """
    The Integrations API is intended for use by ProjectManager and its
    business development partners. Please contact ProjectManager's sales
    team to request use of this API.
    """

    id: object | None = None
    integrationShortId: object | None = None
    config: object | None = None
    enabledBy: object | None = None
    createDate: object | None = None
    modifyDate: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
