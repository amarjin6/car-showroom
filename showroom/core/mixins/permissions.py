from rest_framework.viewsets import ModelViewSet


class ActivityViewSet(ModelViewSet):

    def get_permissions(self, permissions_mapping):
        for actions in permissions_mapping:
            if self.action in actions:
                self.permission_classes = permissions_mapping[actions]
        return self.permission_classes
