#!/usr/bin/python3
""" Nameless module for Console class """
import cmd
import sys
import importlib


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand class.

    Args:
        cmd module's Cmd class it is inheriting from

    Returns:
        Nothing
    """
    intro = ''
    prompt = '(hbnb) '
    module_names = {
        "BaseModel": "base_model",
        "User": "user",
    }
    instances = {}
    err_msg = {
        "no_cls_name": "** class name missing **",
        "no_cls_exist": "** class doesn't exist **",
        "no_inst_id": "** instance id missing **",
        "no_inst_found": "** no instance found **",
        "no_attr_name": "** attribute name missing **",
        "no_attr_value": "** value missing **"
    }

    def print_err(self, key):
        """prints out the appropriate error message
        """
        print(self.err_msg[key])

    def arguments_specified(self, args, num):
        """performs initial checks to ensure class and id are present
        """
        if len(args) == 0:
            self.print_err("no_cls_name")
        else:
            class_name = args[0]
            if class_name not in self.module_names:
                self.print_err("no_cls_exist")
            else:
                if num == 1:
                    return True

                if len(args) == 1:
                    self.print_err("no_inst_id")
                else:
                    instance_id = args[1]
                    if (self.instances.get(class_name) is None or
                            self.instances[class_name].get(instance_id) is None):
                        self.print_err("no_inst_found")
                    else:
                        if num == 2:
                            return True

                        if num == 4:
                            if len(args) == 2:
                                self.print_err("no_attr_name")
                            elif len(args) == 3:
                                self.print_err("no_attr_value")
                            elif len(args) == 4:
                                return True

        return False

    def emptyline(self):
        """Handles empty or whitespace input and overwrites the parent class emptyline method """
        return False

    def do_EOF(self, arg):
        """Exits the console
        """
        return True

    def do_help(self, arg):
        """Prints out the help menu
        """
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit\n")

    def do_quit(self, arg):
        """Quits the console
        """
        return True

    def do_create(self, arg):
        """creates a new class from the arguments specified in the console
        """
        args = arg.split()
        if self.arguments_specified(args, 1) is True:
            class_name = args[0]
            if class_name not in self.instances:
                self.instances[class_name] = {}

            module = importlib.import_module("models." + self.module_names[class_name])
            class_ = getattr(module, class_name)

            new_instance = class_()
            self.instances[class_name][new_instance.id] = new_instance

            # common sense tells me the file will contain multiple class instances' data
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """prints out details of existing class instance
        """
        args = arg.split()
        if self.arguments_specified(args, 2) is True:
            class_name = args[0]
            instance_id = args[1]
            print(self.instances[class_name][instance_id])

    def do_destroy(self, arg):
        """destroys existing class instance
        """
        args = arg.split()
        if self.arguments_specified(args, 2) is True:
            class_name = args[0]
            instance_id = args[1]
            self.instances[class_name][instance_id].remove()
            del self.instances[class_name][instance_id]

    def do_all(self, arg):
        """prints out stringified data of all instances of specified class
        """
        all_list = []
        all_dict = {}

        args = arg.split()
        if len(args) == 0:
            for class_name_key in self.instances:
                all_dict[class_name_key] = []

                if len(self.instances[class_name_key]) > 0:
                    for instance_id_key in self.instances[class_name_key]:
                        all_list.append(str(self.instances[class_name_key][instance_id_key]))

                    print(all_list)
        elif len(args) == 1:
            if self.arguments_specified(args, 1) is True:
                class_name = args[0]

                if class_name in self.instances:
                    if len(self.instances[class_name]) > 0:
                        for instance_id_key in self.instances[class_name]:
                            all_list.append(str(self.instances[class_name][instance_id_key]))

                        print(all_list)

    def do_update(self, arg):
        """updates specific instance based on args passed in
        """
        args = arg.split()
        if self.arguments_specified(args, 4) is True:
            class_name = args[0]
            instance_id = args[1]
            attr_name = args[2]
            attr_val = args[3]

            instance = self.instances[class_name][instance_id]
            setattr(instance, attr_name, attr_val)
            self.instances[class_name][instance_id] = instance

            self.instances[class_name][instance_id].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
