using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Geometry;
using RosMessageTypes.PandaMove;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class Hand : MonoBehaviour
{
    private ROSConnection ros;
    private int nRobotJoints = 2;
    private string rosServiceName = "hand_sync";
    public ArticulationBody[] jointArticulationBodies;
    public GameObject handJoint;
    private Rigidbody targetRigid;

    // Start is called before the first frame update
    void Start()
    {
        ros = ROSConnection.instance;
        handJoint = GameObject.Find("panda_hand");
        jointArticulationBodies = InitSync.jointArticulationBodies;
        ros.ImplementService<MHandRequest>(rosServiceName, HandSync);
        Debug.Log("hand_sync server ON");
    }
    private MHandResponse HandSync(MHandRequest request)
    {
        Debug.Log("");
        MHandResponse response = new MHandResponse();
        try
        {
            if (request.grasp_state == true)
            {
                GameObject targetObject = GameObject.Find(request.object_name);
                for (int i = 0; i < nRobotJoints; i++)
                {
                    var jointDrive = jointArticulationBodies[8 + i].xDrive;
                    jointDrive.target = (float)request.grasp_size;
                    jointArticulationBodies[8 + i].xDrive = jointDrive;
                }
                targetObject.transform.parent = handJoint.transform;
                targetObject.transform.SetParent(handJoint.transform, true);
                targetRigid = targetObject.GetComponent<Rigidbody>();
                targetRigid.useGravity = false;
                targetRigid.isKinematic = true;

                targetObject.transform.parent = handJoint.transform;

                Debug.Log("Holding Object Completed");

                response.execute_state = 1;
                return response;
            }

            else if (request.grasp_state == false)
            {
                GameObject targetObject = GameObject.Find(request.object_name);
                for (int i = 0; i < nRobotJoints; i++)
                {
                    var jointDrive = jointArticulationBodies[8 + i].xDrive;
                    jointDrive.target = (float)request.grasp_size;
                    jointArticulationBodies[8 + i].xDrive = jointDrive;
                }
                // targetObject.transform.parent = GameObject.Find("Plane").transform;
                Vector3 tempPosition = targetObject.transform.position;
                GameObject baseObject = GameObject.Find("Plane");
                targetObject.transform.SetParent(baseObject.transform, true);
                
                if (targetObject.CompareTag("Untagged"))
                {
                    Debug.Log(request.object_name + " is untagged");
                    targetRigid = targetObject.GetComponent<Rigidbody>();
                    targetRigid.useGravity = true;
                    targetRigid.isKinematic = false;
                    tempPosition.y += (float) 0.002;
                }
                targetObject.transform.position = tempPosition;
                
                Debug.Log("Releasing Object Completed");

                response.execute_state = 1;
                return response;
            }

            else
            {
                Debug.Log("Wrong Hand Type");
                response.execute_state = 0;
                return response;
            }
        }
        catch (Exception ex)
        {
            Debug.Log("Hand Sync Error Occured");
            Debug.Log(ex);
            response.execute_state = 0;
            return response;
        }
    }
    // Update is called once per frame
    void Update()
    {

    }
}
