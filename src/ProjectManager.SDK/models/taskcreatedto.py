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
class TaskCreateDto:
    """
    A Task is an individual element of work that must be performed to
    complete a Project. A Task can have one or more Resources assigned
    to it. Tasks can be linked to other Tasks to indicate whether they
    have a dependency or a connection.
    """

    id: object | None = None
    name: object | None = None
    description: object | None = None
    parentTaskId: object | None = None
    percentComplete: object | None = None
    statusId: object | None = None
    priorityId: object | None = None
    assignees: list[object] | None = None
    plannedStartDate: object | None = None
    plannedFinishDate: object | None = None
    plannedDuration: object | None = None
    plannedEffort: object | None = None
    plannedCost: object | None = None
    actualStartDate: object | None = None
    actualCost: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
