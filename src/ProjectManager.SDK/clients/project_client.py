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
from ProjectManager.SDK.models.projectcreaterequestdto import ProjectCreateRequestDto
from ProjectManager.SDK.models.projectcreateresponsedto import ProjectCreateResponseDto
from ProjectManager.SDK.models.projectdto import ProjectDto
from ProjectManager.SDK.models.projectdtolist import ProjectDtoList
from ProjectManager.SDK.models.projectupdatedto import ProjectUpdateDto

class ProjectClient:
    """
    API methods related to Project
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_projects(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[ProjectDtoList]]:
        """
        Retrieve a list of Projects that match an [OData formatted
        query](https://www.odata.org/).

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $select : str
            Specify which properties should be returned
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/projects"
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_project(self, body: ProjectCreateRequestDto) -> AstroResult[AstroResult[ProjectCreateResponseDto]]:
        """
        Create a new project based on the details provided.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Parameters
        ----------
        body : ProjectCreateRequestDto
            Information about the Project you wish to create
        """
        path = "/api/data/projects"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectCreateResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_project(self, projectId: str) -> AstroResult[AstroResult[ProjectDto]]:
        """
        Retrieves a project based on its unique identifier.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to retrieve.
        """
        path = f"/api/data/projects/{projectId}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_project(self, projectId: str, body: ProjectUpdateDto) -> AstroResult[AstroResult[]]:
        """
        Update an existing Project and replace the values of fields
        specified.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Multiple users can be working on data at the same time. When you
        call an API to update an object, this call is converted into a
        Changeset that is then applied sequentially. You can use
        RetrieveChangeset to see the status of an individual Changeset.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to update
        body : ProjectUpdateDto
            All non-null fields in this object will replace previous
            data within the Project
        """
        path = f"/api/data/projects/{projectId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
