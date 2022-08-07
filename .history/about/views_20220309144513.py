from django.db.models import Sum, Avg, Min, Count, F, Q
from rest_framework.response import Response
from .paginator import CustomPagination
from .serializers import (TeamSerializer,
                          PostTeamSerializer,
                          GetOrganizationSerializer,
                          GetOrganizationNepaliSerializer,
                          TeamNepaliSerializer,
                          HospitalEnglishSerializer,
                          HospitalNepaliSerializer,
                          EquipmentEnglishSerializer,
                          EquipmentNepaliSerializer,
                          ResourceEnglishSerializer,
                          ResourceNepaliSerializer,
                          AchievementEnglishSerializer,
                          AchievementNepaliSerializer,
                          SolveEnglishSerializer,
                          SolveNepaliSerializer,
                          DiscussionSerializer,
                          CommentAndVoteSerializer,
                          HelpRequestSerializer,
                          CommunityMemberNepaliSerializer,
                          CommunityMemberEnglishSerializer,
                          HitCountSerializer,
                          )
from rest_framework import viewsets
from rest_framework import permissions
from .models import Team, Organization, Hospital, Equipment, Resource, Achievement, Solve, Discussion, Choices, \
    HelpRequest, CommunityMember, HitCount
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


class TeamLeadsView(viewsets.ModelViewSet):
    queryset = Team.objects.filter(is_approved=True, member_type='T')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class TeamMembersView(viewsets.ModelViewSet):
    queryset = Team.objects.filter(is_approved=True).exclude(member_type='T')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class TeamLeadsNepaliView(viewsets.ModelViewSet):
    queryset = Team.objects.filter(is_approved=True, member_type='T')
    serializer_class = TeamNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class TeamMembersNepaliView(viewsets.ModelViewSet):
    queryset = Team.objects.filter(is_approved=True).exclude(member_type='T')
    serializer_class = TeamNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = PostTeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = GetOrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class OrganizationNepaliView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = GetOrganizationNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class HospitalEnglishView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['province']


class HospitalNepaliView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['province']


class EquipmentEnglishView(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class EquipmentNepaliView(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPagination
    ordering = ['-id']


class ResourceEnglishVideoView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='VI')
    serializer_class = ResourceEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPagination

    ordering = ['-id']


class ResourceNepaliVideoView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='VI')
    serializer_class = ResourceNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPagination

    ordering = ['-id']


class ResourceEnglishNewsView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='NE')
    serializer_class = ResourceEnglishSerializer
    # pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class ResourceNepaliNewsView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='NE')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ResourceNepaliSerializer
    # pagination_class = CustomPagination
    ordering = ['-id']


class ResourceEnglishArticleView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='AR')
    serializer_class = ResourceEnglishSerializer
    # pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class ResourceNepaliArticleView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='AR')
    serializer_class = ResourceNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPagination
    ordering = ['-id']


class ResourceEnglishAnnouncementView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='AN')
    serializer_class = ResourceEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPagination
    ordering = ['-id']


class ResourceAnnouncementNepaliView(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category='AN')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ResourceNepaliSerializer
    # pagination_class = CustomPagination
    ordering = ['-id']


class AchievementNepaliView(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    ordering = ['-id']


class AchievementEnglishView(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    ordering = ['-id']


class SolveEnglishView(viewsets.ModelViewSet):
    queryset = Solve.objects.all()
    serializer_class = SolveEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    ordering = ['-id']


class SolveNepaliView(viewsets.ModelViewSet):
    queryset = Solve.objects.all()
    serializer_class = SolveNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    ordering = ['-id']


class DiscussionView(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class CommentAndVoteView(viewsets.ModelViewSet):
    queryset = Choices.objects.all()
    serializer_class = CommentAndVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class HelpRequestView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class LiveHelpRequestForOxygenCylinderView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.filter(request_for='OC', request_status='unsolved')
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class LiveHelpRequestForOxygenVentilatorView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.filter(request_for='OV', request_status='unsolved')
    serializer_class = HelpRequestSerializer
    ordering = ['-id']


class LiveHelpRequestForOxygenPlantView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.filter(request_for='OP', request_status='unsolved')
    serializer_class = HelpRequestSerializer
    ordering = ['-id']


class LiveHelpRequestForOtherView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.filter(request_for='other', request_status='unsolved')
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class LiveHelpRequestForDialysisMachineView(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.filter(request_for='DM', request_status='unsolved')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HelpRequestSerializer
    ordering = ['-id']


class CommunityBoardOfDirectorEnglishView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Board of Director')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommunityMemberEnglishSerializer
    ordering = ['-id']


class CommunityTechnicalTeamEnglishView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Technical Team')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommunityMemberEnglishSerializer
    ordering = ['-id']


class CommunityAdvisoryCommittteeEnglishView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Advisory Committee')
    serializer_class = CommunityMemberEnglishSerializer
    ordering = ['-id']


class CommunityManagementCommitteeEnglishView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Management Committee')
    serializer_class = CommunityMemberEnglishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class CommunityBoardOfDirectorNepaliView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Board of Director')
    serializer_class = CommunityMemberNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class CommunityTechnicalTeamNepaliView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Technical Team')
    serializer_class = CommunityMemberNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class CommunityAdvisoryCommittteeNepaliView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Advisory Committee')
    serializer_class = CommunityMemberNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class CommunityManagementCommitteeNepaliView(viewsets.ModelViewSet):
    queryset = CommunityMember.objects.filter(community='Management Committee')
    serializer_class = CommunityMemberNepaliSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering = ['-id']


class HitCountView(viewsets.ModelViewSet):
    queryset = HitCount.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HitCountSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        HitCount.objects.filter(pk=instance.id).update(visits=F('visits') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)