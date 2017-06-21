from VirtualMachine import VirtualMachine
from Task import Task

class VirtualMachineService:

    def __init__(self):
        self.RESOURCE_VM = '/vms/'
        self.RESOURCE_VM_PWR_STATE = '/set_power_state/'

    def createVM(self, conn, data):
        pass

    def getVM(self, conn, uuid):
        vmDictionary = conn.get(self.RESOURCE_VM + uuid)
        return VirtualMachine(vmDictionary)

    def getVMS(self, conn):
        vmList = []
        vmDictionary = conn.get(self.RESOURCE_VM)

        for vm in vmDictionary['entities']:
             vmList.append(VirtualMachine(vm))

        return vmList

    def deleteVM(self, conn, vm):
        task_dictionary = conn.get(self.RESOURCE_VM + vm.uuid())
        return Task(task_dictionary)