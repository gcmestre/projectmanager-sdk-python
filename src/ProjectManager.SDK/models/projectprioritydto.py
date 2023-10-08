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
class ProjectPriorityDto:
    """
    A ProjectPriority is a named priority level used by your business to
    determine how to decide which Tasks are the most important. You can
    name your ProjectPriority levels anything you like and you can
    reorganize the order of the ProjectPriority levels at any time.
    """

    id: object | None = None
    name: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
