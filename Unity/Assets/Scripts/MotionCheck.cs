using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Geometry;
using RosMessageTypes.PandaMove;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class MotionCheck : MonoBehaviour
{
    private ROSConnection ros;
    private string rosServiceName = "motion_check";
    public Dictionary<string, int> newObjectStatus = new Dictionary<string, int>();
    private GameObject newObject;

    // Start is called before the first frame update
    void Start()
    {
        ros = ROSConnection.instance;

        ros.ImplementService<MMotionCheckRequest>(rosServiceName, MotionTypeCheck);

        Debug.Log("motion_check server ON");
    }
    private MMotionCheckResponse MotionTypeCheck(MMotionCheckRequest request)
    {
        MMotionCheckResponse response = new MMotionCheckResponse();
        try
        {
            Debug.Log("Received Motion Type Request");

            if (request.motion_type == "Place")
            {
                // Not Assigned
            }
            else if (request.motion_type == "PickUp")
            {
                // Not Assigned
            }
            else if (request.motion_type == "PutOn")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                GameObject baseObject = GameObject.Find(request.object_2[0]);
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                targetObject.transform.SetParent(baseObject.transform, true);   
                targetRigid.constraints = RigidbodyConstraints.FreezePositionX | RigidbodyConstraints.FreezePositionZ | RigidbodyConstraints.FreezeRotation;               
            }
            else if (request.motion_type == "Before_Chop")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                MeshCollider targetCollider = targetObject.GetComponent<MeshCollider>();
                targetRigid.isKinematic = true;
                targetRigid.useGravity = false;
                targetCollider.convex = false;
            }
            else if (request.motion_type == "After_Chop")
            {
                GameObject originObject = GameObject.Find(request.object_1[0]);
                GameObject targetObject = GameObject.Find("Plane").transform.Find(request.object_2[0]).gameObject;
                Vector3 originPosition = originObject.transform.position;
                targetObject.transform.position = originPosition;
                originObject.SetActive(false);
                targetObject.SetActive(true);
            }
            else if (request.motion_type == "Pour")
            {
                if (request.object_2[0] == "bowl")
                {
                    if (!(newObjectStatus.ContainsKey(request.object_1[0])))
                    {
                        newObjectStatus[request.object_1[0]] = 1;
                    }
                    else if (newObjectStatus.ContainsKey(request.object_1[0]))
                    {
                        newObjectStatus[request.object_1[0]] += 1;
                    }
                    GameObject pourObject = GameObject.Find("Plane").transform.Find(request.object_1[0]).gameObject;
                    Vector3 spreadPosition = GameObject.Find(request.object_2[0]).transform.position;
                    spreadPosition.y += (float)0.02;
                    // spreadObject.transform.position = spreadPosition;
                    // spreadObject.SetActive(true);
                    newObject = Instantiate(pourObject, spreadPosition, Quaternion.identity);
                    newObject.transform.SetParent(GameObject.Find(request.object_2[0]).transform, true);
                    newObject.name = request.object_1[1];
                    newObject.SetActive(true);
                }
            }
            else if (request.motion_type == "Before_Spread")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                MeshCollider targetCollider = targetObject.GetComponent<MeshCollider>();
                targetRigid.isKinematic = true;
                targetRigid.useGravity = false;
                targetCollider.convex = false;
            }
            else if (request.motion_type == "After_Spread")
            {
                GameObject originObject = GameObject.Find(request.object_1[0]);
                // GameObject targetObject = GameObject.Find("Plane").transform.Find(request.object_2[0]).gameObject;
                // Vector3 originPosition = originObject.transform.position;
                // targetObject.transform.position = originPosition;
                originObject.SetActive(false);
                // targetObject.SetActive(true);            
            }
            else if (request.motion_type == "Before_Scoop")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                MeshCollider targetCollider = targetObject.GetComponent<MeshCollider>();
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                targetCollider.convex = false;
                targetRigid.useGravity = false;
                targetRigid.isKinematic = true;
            }
            else if (request.motion_type == "After_Scoop")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                GameObject Scooper = GameObject.Find("scooper");
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                targetObject.transform.SetParent(Scooper.transform, true);
            }
            else if (request.motion_type == "ScoopOn")
            {
                GameObject targetObject = GameObject.Find(request.object_1[0]);
                GameObject baseObject = GameObject.Find(request.object_2[0]);
                Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                MeshCollider targetCollider = targetObject.GetComponent<MeshCollider>();
                Vector3 targetPosition = baseObject.transform.position;
                Quaternion targetOrientation = baseObject.transform.rotation;
                // targetObject.transform.parent = baseObject.transform;
                targetPosition.y += (float) 0.05;
                targetCollider.convex = true;
                targetObject.transform.SetParent(baseObject.transform, true);
                targetObject.transform.position = targetPosition;
                targetObject.transform.rotation = targetOrientation;
                targetRigid.constraints = RigidbodyConstraints.FreezePositionX | RigidbodyConstraints.FreezePositionZ | RigidbodyConstraints.FreezeRotation;
                targetRigid.useGravity = true;
                targetRigid.isKinematic = false;
            }
            else if (request.motion_type == "Before_Scrape")
            {
                GameObject Knife = GameObject.Find("knife");
                for (int objectIndex=0; objectIndex<request.object_1.Length; objectIndex++)
                {
                    GameObject targetObject = GameObject.Find(request.object_1[objectIndex]);
                    Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                    targetObject.transform.SetParent(Knife.transform, true);
                    targetRigid.useGravity = false;
                    targetRigid.isKinematic = true;
                }
            }
            else if (request.motion_type == "After_Scrape")
            {
                GameObject baseObject = GameObject.Find(request.object_2[0]);
                Vector3 targetPosition = baseObject.transform.position;
                targetPosition.y += (float) 0.03;
                for (int objectIndex=0; objectIndex<request.object_1.Length; objectIndex++)
                {
                    GameObject targetObject = GameObject.Find(request.object_1[objectIndex]);
                    Rigidbody targetRigid = targetObject.GetComponent<Rigidbody>();
                    targetObject.transform.SetParent(baseObject.transform, true);
                    targetObject.transform.position = targetPosition;
                    targetObject.transform.rotation = Quaternion.Euler(new Vector3(0, UnityEngine.Random.Range(0, 179), 0));
                    targetRigid.useGravity = true;
                    targetRigid.isKinematic = false;
                }
            }
            else if (request.motion_type == "Stir")
            {
                for (int objectIndex=0; objectIndex<request.object_1.Length; objectIndex++)
                {
                    GameObject tempObject = GameObject.Find(request.object_1[objectIndex]);
                    GameObject baseObject = GameObject.Find("Plane");
                    tempObject.SetActive(false);
                    // tempObject.transform.parent = GameObject.Find("Plane").transform;
                    tempObject.transform.SetParent(baseObject.transform, true);
                }
                GameObject containerObject = GameObject.Find("bowl");
                Vector3 targetPosition = containerObject.transform.position;
                targetPosition.y += (float) 0.03;

                GameObject mixedObject = GameObject.Find("Plane").transform.Find(request.object_2[0]).gameObject;
                mixedObject.transform.SetParent(containerObject.transform, true);
                mixedObject.SetActive(true);
                mixedObject.transform.position = targetPosition;
            }
            else if (request.motion_type == "Activate")
            {                
                string cookedSuffix = "_cooked";
                for (int objectIndex=0; objectIndex<request.object_1.Length; objectIndex++)
                {
                    GameObject targetObject = GameObject.Find(request.object_1[objectIndex]);
                    Debug.Log(request.object_1[objectIndex] + cookedSuffix);
                    targetObject.GetComponent<MeshRenderer>().material = Resources.Load(request.object_1[objectIndex] + cookedSuffix) as Material;
                }
            }
            else if (request.motion_type == "Sandwich")
            {
                GameObject targetObject = GameObject.Find("bread1");
                Vector3 targetPosition = targetObject.transform.position;
                targetPosition.y += (float) 0.03;
                newObject = GameObject.Find("Plane").transform.Find("sandwich").gameObject;
                newObject.transform.position = targetPosition;
                targetObject.SetActive(false);
                newObject.SetActive(true);
            }
            response.execute_state = 1;
            return response;
        }
        catch (Exception ex)
        {
            Debug.Log("MotionCheck Execution Error Occured");
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
