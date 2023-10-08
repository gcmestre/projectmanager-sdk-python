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
class UserRoleDto:
    """
    A UserRole is a name for a privilege level granted to a specific
    User. The 'Global Admin' UserRole is granted to the owner of the
    Workspace, and this UserRole cannot be changed. You can choose which
    UserRole applies to a User within your Workspace.
    """

    id: object | None = None
    name: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
