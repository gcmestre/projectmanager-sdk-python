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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models. import 
from ProjectManager.SDK.models.projectmemberdto import ProjectMemberDto
from ProjectManager.SDK.models.projectmemberdtolist import ProjectMemberDtoList
from ProjectManager.SDK.models.projectmemberroledto import ProjectMemberRoleDto

class ProjectMembersClient:
    """
    API methods related to ProjectMembers
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_members(self, projectId: str, includeAllUsers: bool) -> AstroResult[AstroResult[ProjectMemberDtoList]]:
        """
        Returns a list of membership options for existing members.
        Optionally include users who are not a member yet.

        Parameters
        ----------
        projectId : str
            Reference to the project
        includeAllUsers : bool
            Set to true to include all users in the workspace
        """
        path = f"/api/data/projects/{projectId}/members"
        result = self.client.send_request("GET", path, None, {"includeAllUsers": includeAllUsers}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectMemberDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_user_project_membership(self, projectId: str, userId: str) -> AstroResult[AstroResult[ProjectMemberDto]]:
        """
        Return the membership of a project for a user.

        Parameters
        ----------
        projectId : str
            Reference of Project
        userId : str
            Reference of User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectMemberDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[AstroResult[ProjectMemberDto]]:
        """
        Creates a membership for a user in a project and assigns the
        user appropriate permissions

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        body : ProjectMemberRoleDto
            The permission to set
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectMemberDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[AstroResult[ProjectMemberDto]]:
        """
        Update existing Project Access Control for user for project

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        body : ProjectMemberRoleDto
            The permission to update
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectMemberDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def remove_user_project_membership(self, projectId: str, userId: str) -> AstroResult[AstroResult[]]:
        """
        Deletes Project Member

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
