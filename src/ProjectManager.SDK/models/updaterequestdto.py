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
class UpdateRequestDto:
    """
    Represents an update request for a File within ProjectManager.
    ProjectManager allows you to store Files connected to other elements
    of your Workspace such as a Project or a Discussion. When you upload
    a File, please allow a few moments for the File to be processed and
    verified. ProjectManager may reject File uploads that contain
    problems such as malware. Once a File has completed the upload the
    process, you may retrieve it using the DownloadFile API.
    """

    name: object | None = None
    taskId: object | None = None
    folderId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
